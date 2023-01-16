import random
import numpy as np
import torch


def make_reproducible(seed: int = 1):
    """
    ensures reproducibility over multiple script runs and after restarting the local machine
    """
    # cuda
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.cuda.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    # prints
    torch.set_printoptions(sci_mode=False)
    torch.set_printoptions(threshold=100_000)
    np.set_printoptions(suppress=True)
    print("reproducible with seed", seed)


def seed_worker():
    worker_seed = torch.initial_seed() % 2**32
    np.random.seed(worker_seed)
    random.seed(worker_seed)
