// Survey Database Admin - Frontend JavaScript with Full CRUD

const API_BASE = 'http://localhost:5000/api';
let currentTab = 'papers';
let currentPage = 1;
let currentData = [];
let editingItem = null;
let currentlyEditingCell = null;

// Multi-select state: Map of paper.id → paper object for all checked papers
const selectedPapers = new Map();

// Form field definitions for each entity type
const FORM_FIELDS = {
    'papers': [
        { name: 'short_name', label: 'Short Name', type: 'text', required: true },
        { name: 'title', label: 'Title', type: 'text', required: true },
        { name: 'authors', label: 'Authors', type: 'text', required: true },
        { name: 'month', label: 'Date (YYYY-MM)', type: 'text', required: true, placeholder: '2026-01' },
        { name: 'venue', label: 'Venue', type: 'text', required: true },
        { name: 'category', label: 'Category', type: 'multiselect', required: true,
          options: ['sft', 'rl', 'data_collection', 'data_analysis', 'data_synthesis',
                    'evaluation_datasets', 'training_datasets', 'inference_scaling',
                    'methods_analysis', 'workflow', 'tool', 'memory', 'multi_agent', 'single_agent'] },
        { name: 'abstract', label: 'Abstract', type: 'textarea', required: false },
        { name: 'arxiv_link', label: 'arXiv Link', type: 'url', required: false },
        { name: 'github_link', label: 'GitHub Link', type: 'url', required: false },
        { name: 'huggingface_link', label: 'HuggingFace Link', type: 'url', required: false },
        { name: 'website_link', label: 'Website Link', type: 'url', required: false },
        { name: 'doi_link', label: 'DOI Link', type: 'url', required: false },
        { name: 'openreview_link', label: 'OpenReview Link', type: 'url', required: false }
    ],
    'datasets': [
        { name: 'name', label: 'Dataset Name', type: 'text', required: true },
        { name: 'language', label: 'Language', type: 'text', required: false },
        { name: 'multimodal', label: 'Multimodal', type: 'text', required: false },
        { name: 'repos', label: 'Repos', type: 'text', required: false },
        { name: 'amount', label: 'Amount', type: 'text', required: false },
        { name: 'environment', label: 'Environment', type: 'text', required: false },
        { name: 'category', label: 'Category', type: 'select', required: false, options: ['single-pl', 'multi-pl'] },
        { name: 'github_link', label: 'GitHub Link', type: 'url', required: false },
        { name: 'huggingface_link', label: 'HuggingFace Link', type: 'url', required: false },
        { name: 'website_link', label: 'Website Link', type: 'url', required: false }
    ],
    'training-datasets': [
        { name: 'name', label: 'Dataset Name', type: 'text', required: true },
        { name: 'language', label: 'Language', type: 'text', required: false },
        { name: 'repos', label: 'Repos', type: 'text', required: false },
        { name: 'amount', label: 'Amount', type: 'text', required: false },
        { name: 'github_link', label: 'GitHub Link', type: 'url', required: false },
        { name: 'huggingface_link', label: 'HuggingFace Link', type: 'url', required: false }
    ],
    'sft-methods': [
        { name: 'model_name', label: 'Model Name', type: 'text', required: true },
        { name: 'base_model', label: 'Base Model', type: 'text', required: false },
        { name: 'size', label: 'Size', type: 'text', required: false },
        { name: 'architecture', label: 'Architecture', type: 'text', required: false },
        { name: 'training_scaffold', label: 'Training Scaffold', type: 'text', required: false },
        { name: 'resolution_percent', label: 'Resolution %', type: 'number', required: false },
        { name: 'code_link', label: 'Code Link', type: 'url', required: false },
        { name: 'data_link', label: 'Data Link', type: 'url', required: false },
        { name: 'model_link', label: 'Model Link', type: 'url', required: false }
    ],
    'rl-methods': [
        { name: 'model_name', label: 'Model Name', type: 'text', required: true },
        { name: 'base_model', label: 'Base Model', type: 'text', required: false },
        { name: 'size', label: 'Size', type: 'text', required: false },
        { name: 'architecture', label: 'Architecture', type: 'text', required: false },
        { name: 'training_scaffold', label: 'Training Scaffold', type: 'text', required: false },
        { name: 'reward_type', label: 'Reward Type', type: 'text', required: false },
        { name: 'resolution_percent', label: 'Resolution %', type: 'number', required: false },
        { name: 'code_link', label: 'Code Link', type: 'url', required: false },
        { name: 'data_link', label: 'Data Link', type: 'url', required: false },
        { name: 'model_link', label: 'Model Link', type: 'url', required: false }
    ],
    'foundation-models': [
        { name: 'model_name', label: 'Model Name', type: 'text', required: true },
        { name: 'size', label: 'Size', type: 'text', required: false },
        { name: 'architecture', label: 'Architecture', type: 'text', required: false },
        { name: 'inference_scaffold', label: 'Inference Scaffold', type: 'text', required: false },
        { name: 'reward_type', label: 'Reward Type', type: 'text', required: false },
        { name: 'resolution_percent', label: 'Resolution %', type: 'number', required: false },
        { name: 'code_link', label: 'Code Link', type: 'url', required: false },
        { name: 'model_link', label: 'Model Link', type: 'url', required: false }
    ]
};

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    loadStats();
    loadData('papers', { sort_by: 'month', sort_order: 'desc' });
    initializeFilters();
    renderMonthlyChart();
    
    // Scoped search
    let searchTimeout;
    const searchInput = document.getElementById('global-search');
    const clearBtn = document.getElementById('search-clear');

    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        const q = e.target.value;
        clearBtn.classList.toggle('visible', q.length > 0);
        searchTimeout = setTimeout(() => globalSearch(q), 400);
    });

    // Scope pills — click switches tab AND re-runs current query
    document.querySelectorAll('.scope-pill').forEach(pill => {
        pill.addEventListener('click', () => {
            const tabName = pill.dataset.tab;
            switchTab(tabName);
            const q = searchInput.value.trim();
            if (q) globalSearch(q);
        });
    });

    // Form submission
    document.getElementById('item-form').addEventListener('submit', handleFormSubmit);
});

// Load full collection statistics (always shows totals from DB)
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE}/stats`);
        const data = await response.json();

        window.baseStats = data;   // cache for restoring after search
        applyBaseStats();
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

function applyBaseStats() {
    const data = window.baseStats;
    if (!data) return;
    document.getElementById('stat-papers').textContent = data.papers.total;
    document.getElementById('stat-papers-label').textContent = 'Total Works';
    document.getElementById('stat-data').textContent = data.papers.data_total;
    document.getElementById('stat-data-label').textContent = 'Data';
    document.getElementById('stat-methods').textContent = data.papers.methods_total;
    document.getElementById('stat-methods-label').textContent = 'Methods';
    document.getElementById('stat-analysis').textContent = data.papers.analysis_total;
    document.getElementById('stat-analysis-label').textContent = 'Analysis';
    window.statsData = data;   // keep for chart
}

// Update a single stat card to reflect the current search result count
function updateStatForTab(tab, count) {
    const map = {
        'papers':            { el: 'stat-papers',   label: `Works (filtered)` },
        'datasets':          { el: 'stat-data',     label: `Data (filtered)` },
        'training-datasets': { el: 'stat-data',     label: `Data (filtered)` },
        'sft-methods':       { el: 'stat-methods',  label: `Methods (filtered)` },
        'rl-methods':        { el: 'stat-methods',  label: `Methods (filtered)` },
        'foundation-models': { el: 'stat-methods',  label: `Methods (filtered)` },
    };
    const cfg = map[tab];
    if (!cfg) return;
    document.getElementById(cfg.el).textContent = count;
    if (tab === 'papers') {
        document.getElementById('stat-papers-label').textContent = cfg.label;
    }
}

// Initialize filters
function initializeFilters() {
    // Initialize year options (from 2020 to current year)
    const yearSelect = document.getElementById('filter-year');
    if (yearSelect) {
        const currentYear = new Date().getFullYear();
        for (let year = currentYear; year >= 2020; year--) {
            const option = document.createElement('option');
            option.value = year;
            option.textContent = year;
            yearSelect.appendChild(option);
        }
    }
    
    // Initialize category options
    const categorySelect = document.getElementById('filter-category');
    if (categorySelect) {
        const categories = ['sft', 'rl', 'data_collection', 'data_analysis', 'data_synthesis', 'evaluation_datasets', 'training_datasets', 'inference_scaling', 'methods_analysis', 'workflow', 'tool', 'memory', 'multi_agent', 'single_agent'];
        categories.forEach(cat => {
            const option = document.createElement('option');
            option.value = cat;
            option.textContent = cat;
            categorySelect.appendChild(option);
        });
    }
}

// Apply filters
function applyFilters() {
    const year = document.getElementById('filter-year')?.value;
    const category = document.getElementById('filter-category')?.value;
    const sortBy = document.getElementById('sort-by')?.value || 'month';
    
    const filters = {};
    if (year) filters.year = year;
    if (category) filters.category = category;
    filters.sort_by = sortBy;
    filters.sort_order = 'desc';
    
    loadData(currentTab, filters);
    if (currentTab === 'papers') {
        const chartFilters = {};
        if (year) chartFilters.year = year;
        if (category) chartFilters.category = category;
        renderMonthlyChart(chartFilters);
    }
}

// Switch tab
function switchTab(tabName) {
    currentTab = tabName;
    currentPage = 1;
    selectedPapers.clear();
    updateSelectionBar();

    // Sync scope pills
    document.querySelectorAll('.scope-pill').forEach(pill => {
        pill.classList.toggle('active', pill.dataset.tab === tabName);
    });
    
    // Load data for the tab
    loadData(tabName);
}

// Load data based on current tab
async function loadData(tabName, filters = {}) {
    showLoading();

    const isFiltered = Object.keys(filters).some(k => k !== 'sort_by' && k !== 'sort_order' && filters[k]);

    const endpoint = tabName;
    const params = new URLSearchParams({
        page: currentPage,
        per_page: 50,
        ...filters
    });

    try {
        const response = await fetch(`${API_BASE}/${endpoint}?${params}`);
        const data = await response.json();

        currentData = data.items;
        renderTable(tabName, data.items);
        renderPagination(data);

        // Update stat card with filtered count; restore base stats when unfiltered
        if (isFiltered) {
            updateStatForTab(tabName, data.total);
        } else {
            applyBaseStats();
        }
    } catch (error) {
        console.error('Error loading data:', error);
        showError('Failed to load data');
    }
}

// Show loading state
function showLoading() {
    document.getElementById('table-container').innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
            <p>Loading data...</p>
        </div>
    `;
}

// Show error
function showError(message) {
    document.getElementById('table-container').innerHTML = `
        <div class="loading">
            <p style="color: #e74c3c;">❌ ${message}</p>
        </div>
    `;
}

// Render table based on data type
function renderTable(type, items) {
    const container = document.getElementById('table-container');
    
    if (items.length === 0) {
        container.innerHTML = '<div class="loading"><p>No data found</p></div>';
        return;
    }
    
    let tableHTML = '<table>';
    
    switch (type) {
        case 'papers':
            tableHTML += renderPapersTable(items);
            break;
        case 'datasets':
            tableHTML += renderDatasetsTable(items);
            break;
        case 'training-datasets':
            tableHTML += renderTrainingDatasetsTable(items);
            break;
        case 'sft-methods':
            tableHTML += renderSFTMethodsTable(items);
            break;
        case 'rl-methods':
            tableHTML += renderRLMethodsTable(items);
            break;
        case 'foundation-models':
            tableHTML += renderFoundationModelsTable(items);
            break;
    }
    
    tableHTML += '</table>';
    container.innerHTML = tableHTML;
    
    // Attach inline edit event listeners
    attachInlineEditListeners();
}

// Helper function to escape HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Render categories as badges
function renderCategories(categoryString) {
    if (!categoryString) return '-';
    
    const categories = categoryString.split(',').map(c => c.trim()).filter(c => c);
    return categories.map(cat => `<span class="badge badge-info">${cat}</span>`).join(' ');
}

// Attach inline edit listeners
function attachInlineEditListeners() {
    document.querySelectorAll('.editable-cell').forEach(cell => {
        cell.addEventListener('click', handleCellClick);
    });
    // Bool-toggle cells: single click toggles ✓/✗ and saves immediately
    document.querySelectorAll('.bool-toggle').forEach(cell => {
        cell.addEventListener('click', handleBoolToggle);
    });
}

// Toggle a boolean cell (✓ / ✗) and persist via API
async function handleBoolToggle(e) {
    const cell = e.currentTarget;
    const row = cell.closest('tr');
    if (!row) return;
    const itemId = row.dataset.id;
    const itemType = row.dataset.type;
    const field = cell.dataset.field;

    const current = cell.dataset.value || '';
    const next = (current === 'Yes') ? 'No' : 'Yes';

    cell.dataset.value = next;
    cell.textContent = next;
    cell.classList.toggle('bool-yes', next === 'Yes');
    cell.classList.toggle('bool-no', next === 'No');
    cell.classList.add('cell-saving');

    try {
        const response = await fetch(`${API_BASE}/${itemType}/${itemId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ [field]: next }),
        });
        if (!response.ok) throw new Error('Update failed');
        cell.classList.add('cell-saved');
        setTimeout(() => cell.classList.remove('cell-saved'), 500);
        const item = currentData.find(d => d.id == itemId);
        if (item) item[field] = next;
        showToast('Updated!', 'success');
        loadStats();
    } catch (err) {
        // Revert on failure
        cell.dataset.value = current;
        cell.textContent = current;
        cell.classList.toggle('bool-yes', current === 'Yes');
        cell.classList.toggle('bool-no', current === 'No');
        showToast('Update failed: ' + err.message, 'error');
    } finally {
        cell.classList.remove('cell-saving');
    }
}

// Handle cell click for inline editing
function handleCellClick(e) {
    const cell = e.currentTarget;
    
    // If editing another cell, save first
    if (currentlyEditingCell && currentlyEditingCell !== cell) {
        saveInlineEdit(currentlyEditingCell);
    }
    
    // If clicking the currently editing cell, ignore
    if (cell.classList.contains('editing')) {
        return;
    }
    
    startInlineEdit(cell);
}

// Start inline editing
function startInlineEdit(cell) {
    const field = cell.dataset.field;
    const value = cell.dataset.value || cell.textContent.trim();
    const row = cell.closest('tr');
    const itemId = row.dataset.id;
    const itemType = row.dataset.type;
    
    // Mark as editing
    cell.classList.add('editing');
    row.classList.add('editing-row');
    currentlyEditingCell = cell;
    
    // Save original content
    cell.dataset.originalContent = cell.innerHTML;
    cell.dataset.originalValue = value;
    
    // Create input control based on field type
    let input;
    
    if (field === 'category') {
        // Category uses dropdown selection
        let categories = [];
        if (itemType === 'papers') {
            categories = ['sft', 'rl', 'data_collection', 'data_analysis', 'data_synthesis', 'evaluation_datasets', 'training_datasets', 'inference_scaling', 'methods_analysis', 'workflow', 'tool', 'memory', 'multi_agent', 'single_agent'];
        } else if (itemType === 'datasets') {
            categories = ['single-pl', 'multi-pl'];
        }
        
        input = document.createElement('select');
        input.className = 'inline-edit-select';
        
        // Add empty option
        const emptyOption = document.createElement('option');
        emptyOption.value = '';
        emptyOption.textContent = '-';
        input.appendChild(emptyOption);
        
        categories.forEach(cat => {
            const option = document.createElement('option');
            option.value = cat;
            option.textContent = cat;
            if (cat === value) option.selected = true;
            input.appendChild(option);
        });
    } else if (field === 'title' || field === 'authors') {
        // Long text field
        input = document.createElement('input');
        input.type = 'text';
        input.className = 'inline-edit-input';
        input.value = value;
    } else {
        // Short text field
        input = document.createElement('input');
        input.type = 'text';
        input.className = 'inline-edit-input';
        input.value = value;
    }
    
    // Clear cell and add input control
    cell.innerHTML = '';
    cell.appendChild(input);
    input.focus();
    
    // Select all text (if input field)
    if (input.tagName === 'INPUT') {
        input.select();
    }
    
    // Add event listeners
    input.addEventListener('blur', () => {
        // Delay save to avoid conflict with other click events
        setTimeout(() => {
            if (currentlyEditingCell === cell) {
                saveInlineEdit(cell);
            }
        }, 100);
    });
    
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            saveInlineEdit(cell);
        } else if (e.key === 'Escape') {
            cancelInlineEdit(cell);
        }
    });
}

// Save inline edit
async function saveInlineEdit(cell) {
    if (!cell || !cell.classList.contains('editing')) {
        return;
    }
    
    const input = cell.querySelector('input, select, textarea');
    if (!input) {
        return;
    }
    
    const newValue = input.value.trim();
    const oldValue = cell.dataset.originalValue;
    
    // If value unchanged, cancel edit
    if (newValue === oldValue) {
        cancelInlineEdit(cell);
        return;
    }
    
    const field = cell.dataset.field;
    const row = cell.closest('tr');
    const itemId = row.dataset.id;
    const itemType = row.dataset.type;
    
    // Mark as saving
    cell.classList.add('cell-saving');
    
    try {
        // Build update data
        const updateData = {};
        
        // Special handling for month field (YYYY-MM format)
        if (field === 'month') {
            updateData.month = newValue;
            // Extract year from month and update
            const match = newValue.match(/^(\d{4})-(\d{2})$/);
            if (match) {
                updateData.year = parseInt(match[1]);
            }
        } else {
            updateData[field] = newValue;
        }
        
        // If month field, also update year field
        if (field === 'month' && newValue.match(/^\d{4}-\d{2}$/)) {
            const year = parseInt(newValue.split('-')[0]);
            updateData['year'] = year;
        }
        
        // Send update request
        const response = await fetch(`${API_BASE}/${itemType}/${itemId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updateData),
        });
        
        if (!response.ok) {
            throw new Error('Update failed');
        }
        
        // Update successful
        cell.dataset.value = newValue;
        
        // Restore display
        if (field === 'category') {
            cell.innerHTML = `<span class="badge badge-info">${newValue}</span>`;
        } else if (['size'].includes(field)) {
            cell.innerHTML = `<span class="badge badge-primary">${newValue || '-'}</span>`;
        } else if (['resolution_percent'].includes(field)) {
            cell.innerHTML = `<span class="badge badge-success">${newValue || '-'}</span>`;
        } else if (['reward_type'].includes(field)) {
            cell.innerHTML = `<span class="badge badge-info">${newValue || '-'}</span>`;
        } else if (['model_name', 'name'].includes(field)) {
            cell.innerHTML = `<strong>${newValue}</strong>`;
        } else {
            cell.textContent = newValue;
            cell.title = newValue;
        }
        
        // Add save success animation
        cell.classList.add('cell-saved');
        setTimeout(() => {
            cell.classList.remove('cell-saved');
        }, 500);
        
        showToast('Updated successfully!', 'success');
        
        // Update current data
        const item = currentData.find(d => d.id == itemId);
        if (item) {
            item[field] = newValue;
            
            // If month updated, also update year
            if (field === 'month' && newValue.match(/^\d{4}-\d{2}$/)) {
                item['year'] = parseInt(newValue.split('-')[0]);
            }
        }

        // Refresh stat cards (count may have changed e.g. after category edit)
        loadStats();
        
    } catch (error) {
        // Update failed, restore original content
        cell.innerHTML = cell.dataset.originalContent;
        showToast('Update failed: ' + error.message, 'error');
    } finally {
        // Clean up edit state
        cell.classList.remove('editing', 'cell-saving');
        row.classList.remove('editing-row');
        currentlyEditingCell = null;
    }
}

// Cancel inline edit
function cancelInlineEdit(cell) {
    if (!cell || !cell.classList.contains('editing')) {
        return;
    }
    
    const row = cell.closest('tr');
    
    // Restore original content
    cell.innerHTML = cell.dataset.originalContent;
    
    // Clean up edit state
    cell.classList.remove('editing');
    row.classList.remove('editing-row');
    currentlyEditingCell = null;
}

// Render papers table
function renderPapersTable(items) {
    const sortableColumns = [
        { field: 'short_name', label: 'Short Name', sortable: true },
        { field: 'title', label: 'Title', sortable: true },
        { field: 'authors', label: 'Authors', sortable: true },
        { field: 'month', label: 'Date', sortable: true },
        { field: 'venue', label: 'Venue', sortable: true },
        { field: 'category', label: 'Category', sortable: true, filterable: true },
        { field: 'links', label: 'Links', sortable: false },
        { field: 'actions', label: 'Actions', sortable: false }
    ];

    const allChecked = items.length > 0 && items.every(p => selectedPapers.has(p.id));

    let html = `
        <thead>
            <tr>
                <th class="cb-col">
                    <input type="checkbox" class="paper-checkbox" id="select-all-cb"
                        title="Select all" ${allChecked ? 'checked' : ''}
                        onchange="toggleSelectAll(this)">
                </th>`;

    sortableColumns.forEach(col => {
        if (col.sortable) {
            html += `<th class="sortable-header" data-field="${col.field}">
                ${col.label} <span class="sort-icon"></span>
            </th>`;
        } else {
            html += `<th>${col.label}</th>`;
        }
    });

    html += `</tr>
        </thead>
        <tbody>
    `;

    items.forEach(paper => {
        const displayMonth = paper.month ? paper.month.replace('-', '.') : '';
        const monthValue = paper.month || '';
        const checked = selectedPapers.has(paper.id) ? 'checked' : '';
        html += `
            <tr data-id="${paper.id}" data-type="papers" class="${selectedPapers.has(paper.id) ? 'row-selected' : ''}">
                <td class="cb-col">
                    <input type="checkbox" class="paper-checkbox" data-id="${paper.id}"
                        ${checked} onchange="togglePaperSelection(this, ${paper.id})">
                </td>
                <td><span class="badge badge-primary">${paper.short_name}</span></td>
                <td class="editable-cell truncate" data-field="title" data-value="${escapeHtml(paper.title)}" title="${paper.title}">${paper.title}</td>
                <td class="editable-cell truncate" data-field="authors" data-value="${escapeHtml(paper.authors)}" title="${paper.authors}">${paper.authors}</td>
                <td class="editable-cell" data-field="month" data-value="${monthValue}">${displayMonth}</td>
                <td class="editable-cell truncate" data-field="venue" data-value="${escapeHtml(paper.venue)}" title="${paper.venue}">${paper.venue}</td>
                <td class="editable-cell" data-field="category" data-value="${paper.category}">${renderCategories(paper.category)}</td>
                <td>${renderLinks(paper.links)}</td>
                <td>${renderActionButtons(paper.id, 'papers')}</td>
            </tr>
        `;
    });

    html += '</tbody>';
    
    // Attach column sort event listeners
    setTimeout(() => attachColumnSortListeners('papers'), 100);
    
    return html;
}

// Attach column sort listeners
function attachColumnSortListeners(tableType) {
    const headers = document.querySelectorAll('.sortable-header');
    headers.forEach(header => {
        header.addEventListener('click', () => {
            const field = header.dataset.field;
            handleColumnSort(field, tableType);
        });
    });
}

// Handle column sorting
let currentSortField = null;
let currentSortOrder = 'asc';

function handleColumnSort(field, tableType) {
    // Toggle sort order
    if (currentSortField === field) {
        currentSortOrder = currentSortOrder === 'asc' ? 'desc' : 'asc';
    } else {
        currentSortField = field;
        currentSortOrder = 'asc';
    }
    
    // Update header styles
    document.querySelectorAll('.sortable-header').forEach(th => {
        th.classList.remove('sorted-asc', 'sorted-desc');
    });
    
    const activeHeader = document.querySelector(`.sortable-header[data-field="${field}"]`);
    if (activeHeader) {
        activeHeader.classList.add(`sorted-${currentSortOrder}`);
    }
    
    // Execute sort based on table type
    if (tableType === 'papers') {
        sortPapersData(field, currentSortOrder);
    } else if (tableType === 'datasets') {
        sortDatasetsData(field, currentSortOrder);
    }
}

// Sort papers data
function sortPapersData(field, order) {
    currentData.sort((a, b) => {
        let aVal, bVal;
        
        switch(field) {
            case 'short_name':
                aVal = a.short_name || '';
                bVal = b.short_name || '';
                break;
            case 'title':
                aVal = a.title || '';
                bVal = b.title || '';
                break;
            case 'authors':
                aVal = a.authors || '';
                bVal = b.authors || '';
                break;
            case 'month':
                aVal = a.month || '0000-00';
                bVal = b.month || '0000-00';
                break;
            case 'venue':
                aVal = a.venue || '';
                bVal = b.venue || '';
                break;
            case 'category':
                aVal = a.category || '';
                bVal = b.category || '';
                break;
            default:
                return 0;
        }
        
        // String comparison
        if (typeof aVal === 'string' && typeof bVal === 'string') {
            const comparison = aVal.localeCompare(bVal);
            return order === 'asc' ? comparison : -comparison;
        }
        
        // Numeric comparison
        return order === 'asc' ? (aVal > bVal ? 1 : -1) : (aVal < bVal ? 1 : -1);
    });
    
    // Re-render table
    const tableContainer = document.getElementById('data-table');
    if (tableContainer) {
        tableContainer.innerHTML = renderPapersTable(currentData);
        attachInlineEditListeners();
    }
}

// Sort datasets data
function sortDatasetsData(field, order) {
    currentData.sort((a, b) => {
        let aVal = a[field] || '';
        let bVal = b[field] || '';
        
        // Special handling for numeric fields
        if (field === 'repos' || field === 'amount') {
            aVal = parseFloat(aVal) || 0;
            bVal = parseFloat(bVal) || 0;
        }
        
        // Compare
        if (typeof aVal === 'string' && typeof bVal === 'string') {
            const comparison = aVal.localeCompare(bVal);
            return order === 'asc' ? comparison : -comparison;
        }
        
        return order === 'asc' ? (aVal > bVal ? 1 : -1) : (aVal < bVal ? 1 : -1);
    });
    
    // Re-render table
    const tableContainer = document.getElementById('data-table');
    if (tableContainer) {
        tableContainer.innerHTML = renderDatasetsTable(currentData);
        attachInlineEditListeners();
    }
}

// Render datasets table
function renderDatasetsTable(items) {
    const sortableColumns = [
        { field: 'name', label: 'Name', sortable: true },
        { field: 'language', label: 'Language', sortable: true, filterable: true },
        { field: 'multimodal', label: 'Multimodal', sortable: false },
        { field: 'environment', label: 'Environment', sortable: false },
        { field: 'repos', label: 'Repos', sortable: true },
        { field: 'amount', label: 'Amount', sortable: true },
        { field: 'category', label: 'Category', sortable: true, filterable: true },
        { field: 'links', label: 'Links', sortable: false },
        { field: 'actions', label: 'Actions', sortable: false }
    ];
    
    let html = `
        <thead>
            <tr>`;
    
    sortableColumns.forEach(col => {
        if (col.sortable) {
            html += `<th class="sortable-header" data-field="${col.field}">
                ${col.label} <span class="sort-icon"></span>
            </th>`;
        } else {
            html += `<th>${col.label}</th>`;
        }
    });
    
    html += `</tr>
        </thead>
        <tbody>
    `;
    
    items.forEach(dataset => {
        const mm = dataset.multimodal || '';
        const env = dataset.environment || '';
        const mmDisplay = mm === 'Yes' ? 'Yes' : 'No';
        const envDisplay = env === 'Yes' ? 'Yes' : 'No';
        html += `
            <tr data-id="${dataset.id}" data-type="datasets">
                <td><strong>${dataset.name}</strong></td>
                <td class="editable-cell" data-field="language" data-value="${dataset.language || ''}">${dataset.language || '-'}</td>
                <td class="bool-toggle ${mmDisplay === 'Yes' ? 'bool-yes' : 'bool-no'}" data-field="multimodal" data-value="${mmDisplay}" title="Click to toggle">${mmDisplay}</td>
                <td class="bool-toggle ${envDisplay === 'Yes' ? 'bool-yes' : 'bool-no'}" data-field="environment" data-value="${envDisplay}" title="Click to toggle">${envDisplay}</td>
                <td class="editable-cell" data-field="repos" data-value="${dataset.repos || ''}">${dataset.repos || '-'}</td>
                <td class="editable-cell" data-field="amount" data-value="${dataset.amount || ''}">${dataset.amount || '-'}</td>
                <td class="editable-cell" data-field="category" data-value="${dataset.category || ''}"><span class="badge badge-info">${dataset.category || '-'}</span></td>
                <td>${renderLinks(dataset.links)}</td>
                <td>${renderActionButtons(dataset.id, 'datasets')}</td>
            </tr>
        `;
    });
    
    html += '</tbody>';
    
    // Attach column sort event listeners
    setTimeout(() => attachColumnSortListeners('datasets'), 100);
    
    return html;
}

// Render training datasets table
function renderTrainingDatasetsTable(items) {
    let html = `
        <thead>
            <tr>
                <th>Name</th>
                <th>Language</th>
                <th>Repos</th>
                <th>Amount</th>
                <th>Links</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
    `;
    
    items.forEach(dataset => {
        html += `
            <tr data-id="${dataset.id}" data-type="training-datasets">
                <td class="editable-cell" data-field="name" data-value="${escapeHtml(dataset.name || '')}"><strong>${escapeHtml(dataset.name)}</strong></td>
                <td class="editable-cell" data-field="language" data-value="${dataset.language || ''}">${dataset.language || '-'}</td>
                <td class="editable-cell" data-field="repos" data-value="${dataset.repos || ''}">${dataset.repos || '-'}</td>
                <td class="editable-cell" data-field="amount" data-value="${dataset.amount || ''}">${dataset.amount || '-'}</td>
                <td>${renderLinks(dataset.links)}</td>
                <td>${renderActionButtons(dataset.id, 'training-datasets')}</td>
            </tr>
        `;
    });
    
    html += '</tbody>';
    setTimeout(() => attachInlineEditListeners(), 100);
    return html;
}

// Render SFT methods table
function renderSFTMethodsTable(items) {
    let html = `
        <thead>
            <tr>
                <th>Model Name</th>
                <th>Base Model</th>
                <th>Size</th>
                <th>Architecture</th>
                <th>Training Scaffold</th>
                <th>Resolution %</th>
                <th>Links</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
    `;
    
    items.forEach(method => {
        html += `
            <tr data-id="${method.id}" data-type="sft-methods">
                <td class="editable-cell" data-field="model_name" data-value="${escapeHtml(method.model_name || '')}"><strong>${escapeHtml(method.model_name)}</strong></td>
                <td class="editable-cell" data-field="base_model" data-value="${escapeHtml(method.base_model || '')}">${escapeHtml(method.base_model) || '-'}</td>
                <td class="editable-cell" data-field="size" data-value="${method.size || ''}"><span class="badge badge-primary">${method.size || '-'}</span></td>
                <td class="editable-cell" data-field="architecture" data-value="${method.architecture || ''}">${method.architecture || '-'}</td>
                <td class="editable-cell truncate" data-field="training_scaffold" data-value="${escapeHtml(method.training_scaffold || '')}">${escapeHtml(method.training_scaffold) || '-'}</td>
                <td class="editable-cell" data-field="resolution_percent" data-value="${method.resolution_percent || ''}"><span class="badge badge-success">${method.resolution_percent || '-'}</span></td>
                <td>${renderLinks(method.links)}</td>
                <td>${renderActionButtons(method.id, 'sft-methods')}</td>
            </tr>
        `;
    });
    
    html += '</tbody>';
    setTimeout(() => attachInlineEditListeners(), 100);
    return html;
}

// Render RL methods table
function renderRLMethodsTable(items) {
    let html = `
        <thead>
            <tr>
                <th>Model Name</th>
                <th>Base Model</th>
                <th>Size</th>
                <th>Architecture</th>
                <th>Reward Type</th>
                <th>Resolution %</th>
                <th>Links</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
    `;
    
    items.forEach(method => {
        html += `
            <tr data-id="${method.id}" data-type="rl-methods">
                <td class="editable-cell" data-field="model_name" data-value="${escapeHtml(method.model_name || '')}"><strong>${escapeHtml(method.model_name)}</strong></td>
                <td class="editable-cell" data-field="base_model" data-value="${escapeHtml(method.base_model || '')}">${escapeHtml(method.base_model) || '-'}</td>
                <td class="editable-cell" data-field="size" data-value="${method.size || ''}"><span class="badge badge-primary">${method.size || '-'}</span></td>
                <td class="editable-cell" data-field="architecture" data-value="${method.architecture || ''}">${method.architecture || '-'}</td>
                <td class="editable-cell" data-field="reward_type" data-value="${method.reward_type || ''}"><span class="badge badge-info">${method.reward_type || '-'}</span></td>
                <td class="editable-cell" data-field="resolution_percent" data-value="${method.resolution_percent || ''}"><span class="badge badge-success">${method.resolution_percent || '-'}</span></td>
                <td>${renderLinks(method.links)}</td>
                <td>${renderActionButtons(method.id, 'rl-methods')}</td>
            </tr>
        `;
    });
    
    html += '</tbody>';
    setTimeout(() => attachInlineEditListeners(), 100);
    return html;
}

// Render foundation models table
function renderFoundationModelsTable(items) {
    let html = `
        <thead>
            <tr>
                <th>Model Name</th>
                <th>Size</th>
                <th>Architecture</th>
                <th>Inference Scaffold</th>
                <th>Resolution %</th>
                <th>Links</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
    `;
    
    items.forEach(model => {
        html += `
            <tr data-id="${model.id}" data-type="foundation-models">
                <td class="editable-cell" data-field="model_name" data-value="${escapeHtml(model.model_name || '')}"><strong>${escapeHtml(model.model_name)}</strong></td>
                <td class="editable-cell" data-field="size" data-value="${model.size || ''}"><span class="badge badge-primary">${model.size || '-'}</span></td>
                <td class="editable-cell" data-field="architecture" data-value="${model.architecture || ''}">${model.architecture || '-'}</td>
                <td class="editable-cell truncate" data-field="inference_scaffold" data-value="${escapeHtml(model.inference_scaffold || '')}">${escapeHtml(model.inference_scaffold) || '-'}</td>
                <td class="editable-cell" data-field="resolution_percent" data-value="${model.resolution_percent || ''}"><span class="badge badge-success">${model.resolution_percent || '-'}</span></td>
                <td>${renderLinks(model.links)}</td>
                <td>${renderActionButtons(model.id, 'foundation-models')}</td>
            </tr>
        `;
    });
    
    html += '</tbody>';
    setTimeout(() => attachInlineEditListeners(), 100);
    return html;
}

// Render action buttons
function renderActionButtons(id, type) {
    return `
        <div class="action-buttons">
            <button class="action-btn action-btn-edit" onclick="openEditModal(${id}, '${type}')">✏️ Edit</button>
            <button class="action-btn action-btn-delete" onclick="deleteItem(${id}, '${type}')">🗑️ Delete</button>
        </div>
    `;
}

// Render links
function renderLinks(links) {
    if (!links) return '-';
    
    let html = '<div class="link-buttons">';
    
    if (links.github) {
        html += `<a href="${links.github}" class="link-button link-github" target="_blank">GitHub</a>`;
    }
    if (links.huggingface) {
        const hfLinks = links.huggingface.split(', ');
        hfLinks.forEach((link, i) => {
            html += `<a href="${link}" class="link-button link-huggingface" target="_blank">HF${hfLinks.length > 1 ? ` ${i+1}` : ''}</a>`;
        });
    }
    if (links.arxiv) {
        html += `<a href="${links.arxiv}" class="link-button link-arxiv" target="_blank">arXiv</a>`;
    }
    if (links.website) {
        html += `<a href="${links.website}" class="link-button link-website" target="_blank">Website</a>`;
    }
    if (links.code) {
        html += `<a href="${links.code}" class="link-button link-github" target="_blank">Code</a>`;
    }
    if (links.data) {
        html += `<a href="${links.data}" class="link-button link-huggingface" target="_blank">Data</a>`;
    }
    if (links.model) {
        html += `<a href="${links.model}" class="link-button link-huggingface" target="_blank">Model</a>`;
    }
    
    html += '</div>';
    return html !== '<div class="link-buttons"></div>' ? html : '-';
}

// Render pagination
function renderPagination(data) {
    const container = document.getElementById('pagination');
    
    if (data.pages <= 1) {
        container.innerHTML = '';
        return;
    }
    
    let html = '';
    
    // Previous button
    html += `<button ${data.page === 1 ? 'disabled' : ''} onclick="changePage(${data.page - 1})">Previous</button>`;
    
    // Page numbers
    for (let i = 1; i <= Math.min(data.pages, 10); i++) {
        html += `<button class="${i === data.page ? 'active' : ''}" onclick="changePage(${i})">${i}</button>`;
    }
    
    if (data.pages > 10) {
        html += '<button disabled>...</button>';
    }
    
    // Next button
    html += `<button ${data.page === data.pages ? 'disabled' : ''} onclick="changePage(${data.page + 1})">Next</button>`;
    
    container.innerHTML = html;
}

// Change page
function changePage(page) {
    currentPage = page;
    loadData(currentTab);
}

// Global search
function clearSearch() {
    const input = document.getElementById('global-search');
    input.value = '';
    document.getElementById('search-clear').classList.remove('visible');
    applyBaseStats();
    loadData(currentTab, { sort_by: 'month', sort_order: 'desc' });
    renderMonthlyChart();
}

async function globalSearch(query) {
    if (!query) {
        clearSearch();
        return;
    }

    // Use the per-tab endpoint with search param for scoped, accurate results
    try {
        const params = new URLSearchParams({ search: query, page: 1, per_page: 200 });
        const response = await fetch(`${API_BASE}/${currentTab}?${params}`);
        const data = await response.json();

        currentData = data.items;
        renderTable(currentTab, data.items);
        document.getElementById('pagination').innerHTML = '';

        // Reflect search hit count in the stat card
        updateStatForTab(currentTab, data.total);

        // Refresh chart with search filter if on papers tab
        if (currentTab === 'papers') {
            renderMonthlyChart({ search: query });
        }
    } catch (error) {
        console.error('Search error:', error);
    }
}

// ============================================================================
// CRUD Operations
// ============================================================================

// Open add modal
function openAddModal() {
    editingItem = null;
    document.getElementById('modal-title').textContent = 'Add New Item';
    buildForm(currentTab, null);
    showModal();
}

// Open edit modal
async function openEditModal(id, type) {
    try {
        const response = await fetch(`${API_BASE}/${type}/${id}`);
        const item = await response.json();
        
        editingItem = { id, type };
        document.getElementById('modal-title').textContent = 'Edit Item';
        buildForm(type, item);
        showModal();
    } catch (error) {
        showToast('Error loading item: ' + error.message, 'error');
    }
}

// Build form based on entity type
function buildForm(type, data) {
    const fields = FORM_FIELDS[type];
    const formFields = document.getElementById('form-fields');
    
    let html = '';
    
    fields.forEach(field => {
        const value = data ? (data[field.name] || '') : '';
        
        html += `<div class="form-group">`;
        html += `<label for="${field.name}">${field.label}${field.required ? ' *' : ''}</label>`;
        
        if (field.type === 'textarea') {
            html += `<textarea id="${field.name}" name="${field.name}" ${field.required ? 'required' : ''}>${value}</textarea>`;
        } else if (field.type === 'multiselect') {
            // Comma-separated value → set of selected tokens
            const selected = new Set((value || '').split(',').map(s => s.trim()).filter(Boolean));
            html += `<div class="multiselect-grid" id="ms_${field.name}">`;
            field.options.forEach(opt => {
                const chkId = `ms_${field.name}_${opt}`;
                const checked = selected.has(opt) ? 'checked' : '';
                html += `<span class="multiselect-pill">
                    <input type="checkbox" id="${chkId}" value="${opt}" ${checked}>
                    <label for="${chkId}">${opt}</label>
                </span>`;
            });
            html += `</div>`;
        } else if (field.type === 'select') {
            html += `<select id="${field.name}" name="${field.name}" ${field.required ? 'required' : ''}>`;
            html += `<option value="">-- Select --</option>`;
            field.options.forEach(option => {
                html += `<option value="${option}" ${value === option ? 'selected' : ''}>${option}</option>`;
            });
            html += `</select>`;
        } else {
            const placeholder = field.placeholder ? `placeholder="${field.placeholder}"` : '';
            if (type === 'papers' && field.name === 'arxiv_link') {
                html += `<div class="input-with-button">
                    <input type="${field.type}" id="${field.name}" name="${field.name}" value="${value}" ${field.required ? 'required' : ''} ${placeholder}>
                    <button type="button" class="btn-fetch-arxiv" onclick="fetchArxivInfo()">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Fetch
                    </button>
                </div>`;
            } else {
                html += `<input type="${field.type}" id="${field.name}" name="${field.name}" value="${value}" ${field.required ? 'required' : ''} ${placeholder}>`;
            }
        }
        
        html += `</div>`;
    });
    
    formFields.innerHTML = html;
    
    // Add event listeners for arXiv auto-formatting (only for papers)
    if (type === 'papers') {
        setTimeout(() => {
            const arxivLinkInput = document.getElementById('arxiv_link');
            
            if (arxivLinkInput) {
                arxivLinkInput.addEventListener('blur', autoFormatArxivVenue);
                arxivLinkInput.addEventListener('input', autoFormatArxivVenue);
            }
        }, 100);
    }
}

// Handle form submission
async function handleFormSubmit(e) {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const data = {};
    
    formData.forEach((value, key) => {
        if (value) {
            data[key] = value;
        }
    });

    // Collect multiselect fields (checkboxes not included in FormData when unchecked)
    const fields = FORM_FIELDS[currentTab] || [];
    fields.forEach(field => {
        if (field.type === 'multiselect') {
            const container = document.getElementById(`ms_${field.name}`);
            if (container) {
                const checked = [...container.querySelectorAll('input[type="checkbox"]:checked')]
                    .map(cb => cb.value);
                data[field.name] = checked.join(', ');
            }
        }
    });

    // For papers: auto-derive year from month so the backend never gets a missing year error
    if (currentTab === 'papers' && data.month && !data.year) {
        const m = data.month.match(/^(\d{4})-\d{2}$/);
        if (m) data.year = parseInt(m[1]);
    }
    
    try {
        let response;
        
        if (editingItem) {
            // Update existing item
            response = await fetch(`${API_BASE}/${editingItem.type}/${editingItem.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
        } else {
            // Create new item
            response = await fetch(`${API_BASE}/${currentTab}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
        }
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to save item');
        }
        
        closeModal();
        showToast(editingItem ? 'Item updated successfully!' : 'Item added successfully!', 'success');
        loadData(currentTab);
        loadStats();
    } catch (error) {
        showToast('Error: ' + error.message, 'error');
    }
}

// Delete item
async function deleteItem(id, type) {
    if (!confirm('Are you sure you want to delete this item?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/${type}/${id}`, {
            method: 'DELETE',
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to delete item');
        }
        
        showToast('Item deleted successfully!', 'success');
        loadData(currentTab);
        loadStats();
    } catch (error) {
        showToast('Error: ' + error.message, 'error');
    }
}

// Show modal
function showModal() {
    document.getElementById('modal').classList.add('show');
}

// Close modal
function closeModal() {
    document.getElementById('modal').classList.remove('show');
    editingItem = null;
}

// Show toast notification
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// ============================================================
// Multi-select helpers
// ============================================================

function togglePaperSelection(checkbox, paperId) {
    const paper = currentData.find(p => p.id === paperId);
    if (!paper) return;
    if (checkbox.checked) {
        selectedPapers.set(paperId, paper);
    } else {
        selectedPapers.delete(paperId);
    }
    // Highlight row
    const row = checkbox.closest('tr');
    if (row) row.classList.toggle('row-selected', checkbox.checked);
    updateSelectionBar();
    // Keep select-all in sync
    const allCb = document.getElementById('select-all-cb');
    if (allCb) {
        allCb.checked = currentData.length > 0 && currentData.every(p => selectedPapers.has(p.id));
    }
}

function toggleSelectAll(checkbox) {
    currentData.forEach(paper => {
        if (checkbox.checked) {
            selectedPapers.set(paper.id, paper);
        } else {
            selectedPapers.delete(paper.id);
        }
    });
    // Update row highlights and individual checkboxes
    document.querySelectorAll('.paper-checkbox[data-id]').forEach(cb => {
        const id = parseInt(cb.dataset.id);
        cb.checked = checkbox.checked;
        const row = cb.closest('tr');
        if (row) row.classList.toggle('row-selected', checkbox.checked);
    });
    updateSelectionBar();
}

function clearSelection() {
    selectedPapers.clear();
    document.querySelectorAll('.paper-checkbox').forEach(cb => { cb.checked = false; });
    document.querySelectorAll('tr.row-selected').forEach(r => r.classList.remove('row-selected'));
    updateSelectionBar();
}

function updateSelectionBar() {
    const bar = document.getElementById('selection-bar');
    const countEl = document.getElementById('selection-count');
    if (!bar) return;
    const n = selectedPapers.size;
    if (n > 0 && currentTab === 'papers') {
        bar.style.display = 'flex';
        countEl.textContent = `${n} paper${n > 1 ? 's' : ''} selected`;
    } else {
        bar.style.display = 'none';
    }
}

function getPrimaryLink(paper) {
    const links = paper.links || {};
    let link = links.arxiv || links.openreview || links.doi || links.website || links.github || '';
    // Convert arXiv abstract page → PDF for direct reading / NotebookLM
    if (link && link.includes('arxiv.org')) {
        link = link.replace(/arxiv\.org\/(abs|html)\//, 'arxiv.org/pdf/');
    }
    return link;
}

function exportSelectedCSV() {
    if (selectedPapers.size === 0) {
        showToast('No papers selected', 'error');
        return;
    }
    // Selected papers first (in current sort order), then rest
    const selectedIds = new Set(selectedPapers.keys());
    const ordered = [
        ...currentData.filter(p => selectedIds.has(p.id)),
        ...currentData.filter(p => !selectedIds.has(p.id))
    ];
    const headers = ['short_name', 'title', 'authors', 'month', 'venue', 'category',
                     'arxiv', 'github', 'huggingface', 'website', 'doi', 'openreview'];
    let csv = headers.join(',') + '\n';
    ordered.forEach(p => {
        const links = p.links || {};
        const row = [
            p.short_name, p.title, p.authors, p.month || '', p.venue, p.category,
            links.arxiv || '', links.github || '', links.huggingface || '',
            links.website || '', links.doi || '', links.openreview || ''
        ].map(v => `"${String(v || '').replace(/"/g, '""')}"`);
        csv += row.join(',') + '\n';
    });
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `selected_papers_${new Date().toISOString().slice(0,10)}.csv`;
    a.click();
    URL.revokeObjectURL(url);
    showToast(`Exported ${selectedPapers.size} selected paper(s) as CSV`, 'success');
}

function copySelectedLinks() {
    if (selectedPapers.size === 0) {
        showToast('No papers selected', 'error');
        return;
    }
    // Maintain current table order for selected papers
    const selectedIds = new Set(selectedPapers.keys());
    const lines = currentData
        .filter(p => selectedIds.has(p.id))
        .map(p => getPrimaryLink(p))
        .filter(Boolean);

    if (lines.length === 0) {
        showToast('Selected papers have no links', 'error');
        return;
    }
    navigator.clipboard.writeText(lines.join('\n')).then(() => {
        showToast('Copied! You can paste into NotebookLM to explore.', 'success');
    }).catch(() => {
        // Fallback for older browsers
        const ta = document.createElement('textarea');
        ta.value = lines.join('\n');
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast('Copied! You can paste into NotebookLM to explore.', 'success');
    });
}

// Export data
function exportData(format) {
    if (currentData.length === 0) {
        alert('No data to export');
        return;
    }
    
    let content = '';
    let filename = `${currentTab}_export.${format}`;
    
    if (format === 'csv') {
        content = exportToCSV(currentData);
    } else {
        alert('Only CSV export is supported');
        return;
    }
    
    // Download file
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}

// Export to CSV
function exportToCSV(data) {
    if (data.length === 0) return '';
    
    const headers = Object.keys(data[0]).filter(key => typeof data[0][key] !== 'object');
    let csv = headers.join(',') + '\n';
    
    data.forEach(row => {
        const values = headers.map(header => {
            const value = row[header] || '';
            return `"${String(value).replace(/"/g, '""')}"`;
        });
        csv += values.join(',') + '\n';
    });
    
    return csv;
}

// Parse arXiv ID from link
function parseArxivId(link) {
    if (!link) return null;
    
    // Match arxiv.org/abs/XXXX.XXXXX or arxiv.org/pdf/XXXX.XXXXX or arxiv.org/html/XXXX.XXXXX
    const match = link.match(/arxiv\.org\/(abs|pdf|html)\/(\d{4}\.\d{4,5})/i);
    if (match) {
        return match[2]; // Return the arXiv ID (e.g., "2601.13713")
    }
    return null;
}

// Generate arXiv venue format (without year suffix)
function generateArxivVenue(arxivId, year=null) {
    if (!arxivId) return '';
    return `arXiv preprint arXiv:${arxivId}`;
}

// Auto-format arXiv venue when arXiv link is provided
function autoFormatArxivVenue() {
    const arxivLinkInput = document.getElementById('arxiv_link');
    const venueInput = document.getElementById('venue');
    
    if (!arxivLinkInput || !venueInput) return;
    
    const arxivLink = arxivLinkInput.value.trim();
    const currentVenue = venueInput.value.trim();
    
    // Only auto-format if venue is empty or already in arXiv format
    if (arxivLink && (!currentVenue || currentVenue.startsWith('arXiv preprint'))) {
        const arxivId = parseArxivId(arxivLink);
        if (arxivId) {
            venueInput.value = generateArxivVenue(arxivId);
        }
    }
}

// Sync to data folder
async function syncToData() {
    if (!confirm('Are you sure you want to sync the database to the data folder? This will overwrite existing YAML/CSV files.')) {
        return;
    }
    
    showToast('Syncing...', 'info');
    
    try {
        const response = await fetch(`${API_BASE}/sync-to-data`, {
            method: 'POST'
        });
        
        const result = await response.json();
        
        if (result.success) {
            showToast('✓ Data synced to data folder!', 'success');
        } else {
            showToast('Sync failed: ' + (result.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        showToast('Sync failed: ' + error.message, 'error');
    }
}

// Import from data folder
async function importFromData() {
    if (!confirm('Are you sure you want to import data from the data folder? This may overwrite existing data in the database.')) {
        return;
    }
    
    showToast('Importing...', 'info');
    
    try {
        const response = await fetch(`${API_BASE}/import-from-data`, {
            method: 'POST'
        });
        
        const result = await response.json();
        
        if (result.success) {
            showToast('✓ Data imported from data folder!', 'success');
            // Refresh page data
            loadData(currentTab);
            loadStats();
        } else {
            showToast('Import failed: ' + (result.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        showToast('Import failed: ' + error.message, 'error');
    }
}

// Toggle visualization
let chartInstance = null;
let chartRange = 'all';
let fullChartData = [];

function toggleVisualization() {
    const vizContainer = document.getElementById('visualization-container');
    const toggleText = document.getElementById('viz-toggle-text');
    const hidden = vizContainer.style.display === 'none';

    if (hidden) {
        vizContainer.style.display = 'block';
        toggleText.textContent = 'Hide Charts';
        renderMonthlyChart();
    } else {
        vizContainer.style.display = 'none';
        toggleText.textContent = 'Show Charts';
    }
}

function changeChartRange(range) {
    chartRange = range;
    
    // Update button state
    document.querySelectorAll('[id^="range-"]').forEach(btn => {
        btn.classList.remove('active');
        btn.style.background = '';
        btn.style.color = '';
    });
    
    const activeBtn = document.getElementById(`range-${range}`);
    if (activeBtn) {
        activeBtn.style.background = '#667eea';
        activeBtn.style.color = 'white';
    }
    
    renderMonthlyChart();
}

// Render monthly publication chart (optionally filtered)
async function renderMonthlyChart(filters = {}) {
    try {
        let monthlyData;
        const hasFilter = filters && Object.keys(filters).some(k => filters[k]);
        if (hasFilter) {
            const params = new URLSearchParams(filters);
            const resp = await fetch(`${API_BASE}/stats/filtered?${params}`);
            const data = await resp.json();
            monthlyData = data.by_month || {};
        } else {
            const response = await fetch(`${API_BASE}/stats`);
            const stats = await response.json();
            monthlyData = stats.papers.by_month || {};
        }
        
        // Convert to array and sort by date
        const monthArray = Object.entries(monthlyData).map(([month, count]) => ({
            month: month,
            count: count,
            sortKey: new Date(month + '-01')  // Convert to date object for sorting
        }));
        
        // Sort by date
        monthArray.sort((a, b) => a.sortKey - b.sortKey);
        
        // Extract sorted data
        const sortedMonths = monthArray.map(item => item.month);
        const counts = monthArray.map(item => item.count);
        
        // Format month labels (2026-01 → 2026.01)
        const labels = sortedMonths.map(month => {
            return month.replace('-', '.');
        });
        
        const ctx = document.getElementById('monthly-chart');
        
        // Destroy old chart
        if (chartInstance) {
            chartInstance.destroy();
        }
        
        // Save full chart data
        fullChartData = { months: sortedMonths, counts: counts, labels: labels };
        
        // Filter data based on selected range
        let displayMonths = sortedMonths;
        let displayCounts = counts;
        let displayLabels = labels;
        
        if (chartRange === 'year' && sortedMonths.length > 12) {
            // Last 12 months
            displayMonths = sortedMonths.slice(-12);
            displayCounts = counts.slice(-12);
            displayLabels = labels.slice(-12);
        } else if (chartRange === 'half' && sortedMonths.length > 6) {
            // Last 6 months
            displayMonths = sortedMonths.slice(-6);
            displayCounts = counts.slice(-6);
            displayLabels = labels.slice(-6);
        }
        
        // Create new chart
        chartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: displayLabels,
                datasets: [{
                    label: 'Papers Published',
                    data: displayCounts,
                    backgroundColor: 'rgba(102, 126, 234, 0.6)',
                    borderColor: 'rgba(102, 126, 234, 1)',
                    borderWidth: 2,
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        display: false
                    },
                    title: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `Papers: ${context.parsed.y}`;
                            }
                        },
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                        padding: 12,
                        titleFont: {
                            size: 14
                        },
                        bodyFont: {
                            size: 14
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 1,
                            font: {
                                size: 12
                            }
                        },
                        title: {
                            display: true,
                            text: 'Number of Papers',
                            font: {
                                size: 14,
                                weight: 'bold'
                            },
                            color: '#666'
                        },
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Publication Month',
                            font: {
                                size: 14,
                                weight: 'bold'
                            },
                            color: '#666'
                        },
                        ticks: {
                            font: {
                                size: 11
                            },
                            maxRotation: 45,
                            minRotation: 45
                        },
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
        
        // Render chart summary
        renderChartSummary(displayCounts, displayMonths);
        
    } catch (error) {
        console.error('Error rendering chart:', error);
        showToast('Chart failed to load', 'error');
    }
}

// Render chart summary
function renderChartSummary(counts, months) {
    const summaryDiv = document.getElementById('chart-summary');
    
    if (counts.length === 0) {
        summaryDiv.innerHTML = '<p>No data available</p>';
        return;
    }
    
    const total = counts.reduce((a, b) => a + b, 0);
    const average = (total / counts.length).toFixed(1);
    const max = Math.max(...counts);
    const maxMonthIndex = counts.indexOf(max);
    const maxMonth = months[maxMonthIndex];
    const maxMonthLabel = maxMonth.replace('-', '.');
    
    summaryDiv.innerHTML = `
        <div style="text-align: center;">
            <div style="font-size: 24px; font-weight: bold; color: #667eea;">${total}</div>
            <div style="font-size: 12px; color: #999; margin-top: 5px;">Total Papers</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 24px; font-weight: bold; color: #667eea;">${average}</div>
            <div style="font-size: 12px; color: #999; margin-top: 5px;">Avg per Month</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 24px; font-weight: bold; color: #667eea;">${max}</div>
            <div style="font-size: 12px; color: #999; margin-top: 5px;">Peak Month</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 16px; font-weight: bold; color: #667eea;">${maxMonthLabel}</div>
            <div style="font-size: 12px; color: #999; margin-top: 5px;">Highest Activity</div>
        </div>
    `;
}

// ============================================================================
// arXiv Fetch, Build Website, Render from DB
// ============================================================================

async function fetchArxivInfo() {
    const arxivLinkInput = document.getElementById('arxiv_link');
    if (!arxivLinkInput || !arxivLinkInput.value.trim()) {
        showToast('Please enter an arXiv link first', 'error');
        return;
    }

    const btn = document.querySelector('.btn-fetch-arxiv');
    const originalContent = btn ? btn.innerHTML : '';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner-small"></span> Fetching...';
    }

    try {
        const response = await fetch(`${API_BASE}/fetch-arxiv`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ arxiv_link: arxivLinkInput.value.trim() })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch arXiv info');
        }

        // Fill form fields
        const titleInput = document.getElementById('title');
        const authorsInput = document.getElementById('authors');
        const venueInput = document.getElementById('venue');
        const yearInput = document.getElementById('year');
        const monthInput = document.getElementById('month');

        if (titleInput) titleInput.value = data.title || '';
        if (authorsInput) authorsInput.value = data.authors || '';
        if (venueInput) venueInput.value = data.venue || '';
        if (yearInput) yearInput.value = data.year || '';
        if (monthInput) monthInput.value = data.month || '';
        if (arxivLinkInput) arxivLinkInput.value = data.arxiv_link || arxivLinkInput.value;

        showToast('arXiv info fetched successfully!', 'success');
    } catch (error) {
        showToast('Error: ' + error.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = originalContent;
        }
    }
}

async function buildWebsite() {
    showToast('Building website...', 'info');

    try {
        const response = await fetch(`${API_BASE}/build-website`, {
            method: 'POST'
        });

        const result = await response.json();

        if (result.success) {
            showToast('✓ Website built successfully!', 'success');
        } else {
            showToast('Build failed: ' + (result.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        showToast('Build failed: ' + error.message, 'error');
    }
}

async function renderFromDB() {
    showToast('Rendering from database...', 'info');

    try {
        const response = await fetch(`${API_BASE}/render-from-db`, {
            method: 'POST'
        });

        const result = await response.json();

        if (result.success) {
            showToast('✓ Rendered from database successfully!', 'success');
        } else {
            showToast('Render failed: ' + (result.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        showToast('Render failed: ' + error.message, 'error');
    }
}
