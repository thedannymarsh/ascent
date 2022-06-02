# Submitting NEURON jobs
We provide scripts for the user to submit NEURON jobs in `src/neuron/`. It
is suggested that the script ending in `“.sh”` is used for Linux-based
cluster contexts; on the other hand, if running locally, the environment
setup will likely be more specific to the machine, and the script ending
in `“.py”` is the better choice. The `submit.sh` acts as a buffer for
`submit.py` to set up the environment and load appropriate modules for job
submission. The `submit.py` script takes the input of the ***Run***
configuration and submits a NEURON call for each independent fiber
within an `n_sim/`. These scripts are called using similar syntax as
`pipeline.py`: `“./submit.<ext> <run indices>,”` where `<run
indices>` is a space-separated list of integers. Note that these
submission scripts expect to be called from a directory with the
structure generated by `Simulation.export_nsims()` at the location
defined by `“ASCENT_NSIM_EXPORT_PATH”` in `env.json`.

## Cluster submissions
When using a high-performance computing cluster running SLURM:
1. Set your default parameters, particularly your partition (can be found in
`"config/system/slurm_params.json"`). The partition you set here (default is "common"
) will apply to all `submit.py` runs. To override this on a per-run basis, pass
the command line argument --partition. (e.g.
`"python submit.py --partition my_partition <run indices>"`)
For more information, see [Command-Line Arguments](command_line_args).
2. Optionally, set your `"submission_context"` to `"auto"`, and configure your `run.json` with the
appropriate hostname prefix. (Only necessary if you plan to submit runs both locally and
on a cluster, see [S8 Text](S8-JSON-file-parameter-guide).)