# Agentic-AI-Notebooks

Collection of Colab Notebooks from the Agentic AI Sessions

## Run this Repo Locally

Firstly install Miniconda from [the Anaconda Website](https://docs.anaconda.com/miniconda/install/).

Then open a command prompt, and run the following. This will create and activate a python 3.11 environment called `crp-learning`.

```bash
conda create -n crp-learning python=3.11.13
conda activate crp-learning
```

After running this, your CMD prompt should have a "`(crp-learning)`" prefixed at the start.

> [!TIP]
> To **deactivate** the environment, simply run:
>
> ```bash
> conda deactivate
> ```
>
> To **remove** the environment completely, run:
>
> ```bash
> conda env remove -n crp-learning
> ```

<br/>

> [!NOTE]
> Remember to select `crp-learning` as the kernel for all the notebooks!

Afterwards, head over to the [`Setup` Notebook](.Setup.ipynb) to start setting up the environment!

---

## Environment Variables

A lot of the models and frameworks used in the notebooks in this repo require a Private Access Token or some sort of Secret Keys.
To make loading them easier, follow these steps:

1. Create a `.env` file following the [example file](.env.example) provided.
2. In the [`Setup` Notebook](.Setup.ipynb), and run the codeblock under the heading `Setting Environment Variables`

The script can be found over in [`utils/env_variables_setup.py`](utils/env_variables_setup.py).

> [!NOTE]
> This script only has to be run once when setting up the environment. Conda environments store the set keys in the environment files
>
> Anytime you update an entry in the `.env` file, you have to run the script to add/update the new/updated variable to the conda environment

### Required API Keys / Private Access Tokens

Here is an ever-growing list of Keys and Private Access Tokens used throughout the notebooks in this repo. Each notebook will also have a list of tokens specific to that notebook.

| Token Name                                                           | `.env` Name          | Where to Get / Setting Value                                                      |                                                                                                                                                                        Reference |
| :------------------------------------------------------------------- | :------------------- | :-------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Hugging Face User Access Token                                       | `HF_TOKEN`           | [Hugging Face Settings](https://huggingface.co/settings/tokens)                   |                                                                                                                                 [Hugging Face Docs](https://huggingface.co/docs) |
| Google Gemini API Key                                                | `GEMINI_API_KEY`     | [Google AI Studio](https://aistudio.google.com/api-keys)                          |                                                                                                              [Gemini API Docs](https://ai.google.dev/gemini-api/docs/quickstart) |
| Google Gemini API Key (Used by the `langchain-google-genai` package) | `GOOGLE_API_KEY`     | [Google AI Studio](https://aistudio.google.com/api-keys)                          | [Gemini API Docs](https://ai.google.dev/gemini-api/docs/quickstart) and [LangChain Google Integration Docs](https://docs.langchain.com/oss/python/integrations/providers/google) |
| OpenAI API Key                                                       | `OPENAI_API_KEY`     | [OpenAI API Platform](https://platform.openai.com/settings/organization/api-keys) |                                                                                              [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction) |
| LangSmith API Key                                                    | `LANGSMITH_API_KEY`  | [LangSmith Settings](https://smith.langchain.com/settings)                        |                                                                                                             [LangSmith API Reference](https://docs.langchain.com/langsmith/home) |
| LangSmith Tracing                                                    | `LANGSMITH_TRACING`  | A Boolean, set the value to `true` or `false` to enable or disable logging traces |                                                                           [LangSmith Observability API Reference](https://docs.langchain.com/langsmith/observability-quickstart) |
| LangSmith Endpoint                                                   | `LANGSMITH_ENDPOINT` | The LangSmith Endpoint to log the traces (<https://api.smith.langchain.com>)      |                                                                           [LangSmith Observability API Reference](https://docs.langchain.com/langsmith/observability-quickstart) |
| LangSmith Project Name                                               | `LANGSMITH_PROJECT`  | The Name of the Project to log the traces under                                   |                                                                           [LangSmith Observability API Reference](https://docs.langchain.com/langsmith/observability-quickstart) |

### [`utils/env_variables_setup.py`](utils/env_variables_setup.py)

This is a simple script with three functions only.

It runs the command line `conda` tool to `set`, `unset`, and `list` the variables.

| Function                            | Description                                                             | CLI Command                           |                                                                                           Reference |
| :---------------------------------- | :---------------------------------------------------------------------- | :------------------------------------ | --------------------------------------------------------------------------------------------------: |
| `set_env_variables(env_file: Path)` | Set an environment variable in the conda environment from the .env file | `conda env config vars set KEY=VALUE` |   [documentation](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/set.html) |
| `unset_env_variable(key: str)`      | Unset an environment variable in the conda environment                  | `conda env config vars unset KEY`     | [documentation](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/unset.html) |
| `list_env_variables()`              | List all environment variables set in the conda environment             | `conda env config vars list`          |  [documentation](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/list.html) |

---
