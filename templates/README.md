# Templates for Batch Import

This folder contains CSV templates for batch importing papers and tables.

## 📄 Paper Template (`papers_template.csv`)

### Column Definitions

| Column | Description | Required | Example |
|--------|-------------|----------|---------|
| `category_id` | Paper category | ✅ | `evaluation_datasets` |
| `short_name` | Short name/identifier | ✅ | `SWE-bench` |
| `title` | Full paper title | ✅ | `SWE-bench: Can Language Models Resolve Real-World GitHub Issues?` |
| `authors` | Author list | ❌ | `Carlos E. Jimenez et al.` |
| `venue` | Publication venue | ❌ | `arXiv 2024` |
| `year` | Publication year | ✅ | `2024` |
| `arxiv` | arXiv URL | ❌ | `https://arxiv.org/abs/2310.06770` |
| `github` | GitHub URL | ❌ | `https://github.com/princeton-nlp/SWE-bench` |
| `huggingface` | HuggingFace URL | ❌ | `-` |
| `openreview` | OpenReview URL | ❌ | `-` |
| `acl` | ACL Anthology URL | ❌ | `-` |
| `doi` | DOI URL | ❌ | `-` |
| `website` | Other website URL | ❌ | `-` |

### Valid Category IDs

- `evaluation_datasets` - 📊 Evaluation Datasets
- `training_datasets` - 🎯 Training Datasets
- `single_agent` - 🤖 Single-Agent Systems
- `multi_agent` - 👥 Multi-Agent Systems
- `workflow` - 🔄 Workflow-Based Methods
- `tool` - 🛠️ Tool-Augmented Methods
- `memory` - 🧠 Memory-Enhanced Methods
- `sft` - 📚 Supervised Fine-Tuning (SFT)
- `rl` - 🎮 Reinforcement Learning (RL)
- `inference_scaling` - ⚡ Inference-Time Scaling
- `data_collection` - 📥 Data Collection Methods
- `data_synthesis` - 🔬 Data Synthesis Methods
- `data_analysis` - 📈 Data Analysis
- `methods_analysis` - 🔍 Methods Analysis

### Usage

1. Open `papers_template.csv` in Excel/LibreOffice/Text Editor
2. Fill in your papers (one row per paper)
3. Save the file
4. Import: `run.bat` → `[3] Batch Import`
5. Or: `python scripts/batch_import.py templates/papers_template.csv`

### Example Data

```csv
category_id,short_name,title,authors,venue,year,arxiv,github,huggingface,openreview,acl,doi,website
evaluation_datasets,SWE-bench,SWE-bench: Can Language Models Resolve Real-World GitHub Issues?,Carlos E. Jimenez et al.,arXiv 2024,2024,https://arxiv.org/abs/2310.06770,https://github.com/princeton-nlp/SWE-bench,-,-,-,-,-
training_datasets,SWE-Gym,Training Software Engineering Agents and Verifiers with SWE-Gym,-,-,2024,-,https://github.com/...,-,-,-,-,-
```

## 📊 Table Templates

We provide 5 specialized table templates for different types of data:

### Table 1: Datasets (`table1_datasets.csv`)

**Columns:** Dataset, Language, Multimodal, Repos, Amount, Environment, Link

For evaluation and training datasets information.

**Example:**
```csv
Dataset,Language,Multimodal,Repos,Amount,Environment,Link
SWE-bench,Python,❌,2294,2294,✅,\ghlink{https://github.com/princeton-nlp/SWE-bench}
```

### Table 2: Trajectory Datasets (`table2_trajectories.csv`)

**Columns:** Dataset, Language, Repos, Amount, Link

For trajectory/annotation datasets used in training.

**Example:**
```csv
Dataset,Language,Repos,Amount,Link
R2E-Gym,Python,10,"3,321",\ghlink{https://github.com/R2E-Gym/R2E-Gym} \hflink{https://huggingface.co/datasets/R2E-Gym/R2EGym-SFT-Trajectories}
```

### Table 3: SFT Models (`table3_sft_models.csv`)

**Columns:** Model Name, Base Model, Size, Arch., Training Scaffold, Res.(%), Code, Data, Model

For Supervised Fine-Tuning models.

**Example:**
```csv
Model Name,Base Model,Size,Arch.,Training Scaffold,Res.(%),Code,Data,Model
SWE-Lego-Qwen3-32B,Qwen3-32B,32B,Dense,OpenHands,57.6,\ghlink{https://github.com/SWE-Lego/SWE-Lego},\hflink{https://huggingface.co/SWE-Lego/datasets},\hflink{https://huggingface.co/SWE-Lego/SWE-Lego-Qwen3-32B}
```

### Table 4: RL Models (`table4_rl_models.csv`)

**Columns:** Model Name, Base Model, Size, Arch., Train. Scaffold, Reward, Res.(%), Code, Data, Model

For Reinforcement Learning models.

**Example:**
```csv
Model Name,Base Model,Size,Arch.,Train. Scaffold,Reward,Res.(%),Code,Data,Model
Kimi-Dev,Qwen 2.5-72B-Base,72B,Dense,BugFixer + TestWriter,Outcome,60.4,\ghlink{https://github.com/MoonshotAI/Kimi-Dev},-,\hflink{https://huggingface.co/moonshotai/Kimi-Dev-72B}
```

### Table 5: General Models (`table5_general_models.csv`)

**Columns:** Model Name, Size, Arch., Inf. Scaffold, Reward, Res.(%), Code, Model

For general-purpose/foundation models (not specifically trained on SWE tasks).

**Example:**
```csv
Model Name,Size,Arch.,Inf. Scaffold,Reward,Res.(%),Code,Model
MiMo-V2-Flash,309B-A15B,MoE,Agentless,Outcome,73.4,\ghlink{https://github.com/XiaomiMiMo/MiMo-V2-Flash},\hflink{https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash}
```

### Special Syntax for Links

- `\ghlink{url}` - GitHub badge
- `\hflink{url}` - HuggingFace badge
- `\bloglink{url}` - Website badge
- `✅` / `❌` - Checkmark / Cross mark

### Data Validation Rules

Each table type has specific validation and sorting rules:

1. **Table 1 (Datasets)**:
   - Auto-categorize into Single-PL vs Multi-PL based on language column
   
2. **Table 2 (Trajectories)**:
   - Auto-sort by Amount (descending)
   
3. **Table 3 (SFT Models)**:
   - Auto-sort by Res.% (resolved rate, descending)
   
4. **Table 4 (RL Models)**:
   - Auto-categorize by parameter size (560B, 72B, 32B, etc.)
   - Auto-sort by Res.% within each category (descending)
   
5. **Table 5 (General Models)**:
   - Auto-sort by Res.% (resolved rate, descending)

### Usage

1. Choose the appropriate template for your data type
2. Open in Excel/LibreOffice/Text Editor
3. Fill in data rows (keep column headers unchanged)
4. Save to `data/tables/` with the corresponding name:
   - `table1_datasets.csv` → `data/tables/table1.csv`
   - `table2_trajectories.csv` → `data/tables/table2.csv`
   - `table3_sft_models.csv` → `data/tables/table3.csv`
   - `table4_rl_models.csv` → `data/tables/table4.csv`
   - `table5_general_models.csv` → `data/tables/table5.csv`
5. Validate and sort: `python scripts/validate_tables.py`
6. Render: `run.bat` → `[2] Add Table`

## 🚀 Quick Start

```bash
# Windows
run.bat → [3] Batch Import

# Linux/Mac
./run.sh → [3] Batch Import
```

## 💡 Tips

1. **Empty Fields**: Use `-` or leave blank for optional fields
2. **Excel Editing**: Open CSV files in Excel for easier editing
3. **UTF-8 Encoding**: Save files as UTF-8 to support special characters
4. **Validation**: Script automatically checks for duplicates
5. **Testing**: Import a few papers first to verify the format

## 📝 Notes

- Lines starting with `#` are treated as comments and ignored
- Duplicate papers are automatically detected and skipped
- All imports can be previewed before confirmation
- Run sync scripts automatically after import

