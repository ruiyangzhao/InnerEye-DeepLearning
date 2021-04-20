#  ------------------------------------------------------------------------------------------
#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License (MIT). See LICENSE in the repo root for license information.
#  ------------------------------------------------------------------------------------------

from InnerEye.SSL.lightning_containers.ssl_container import EncoderName, SSLContainer, SSLDatasetName
from InnerEye.SSL.utils import SSLType


class CIFAR10SimCLR(SSLContainer):
    """
    This module trains an SSL encoder using SimCLR on CIFAR10 and finetunes a linear head on CIFAR10 too.
    """

    def __init__(self) -> None:
        super().__init__(ssl_training_dataset_name=SSLDatasetName.CIFAR10,
                         classifier_dataset_name=SSLDatasetName.CIFAR10,
                         ssl_training_batch_size=512,
                         ssl_encoder=EncoderName.resnet50,
                         ssl_training_type=SSLType.SimCLR,
                         random_seed=1,
                         recovery_checkpoint_save_interval=200,
                         num_epochs=2500,
                         num_workers=6)


class CIFAR10BYOL(SSLContainer):
    """
    This module trains an SSL encoder using BYOL on CIFAR10 and finetunes a linear head on CIFAR10 too.
    """

    def __init__(self) -> None:
        super().__init__(ssl_training_dataset_name=SSLDatasetName.CIFAR10,
                         classifier_dataset_name=SSLDatasetName.CIFAR10,
                         ssl_training_batch_size=512,
                         ssl_encoder=EncoderName.resnet50,
                         ssl_training_type=SSLType.BYOL,
                         random_seed=1,
                         recovery_checkpoint_save_interval=200,
                         num_epochs=2500,
                         num_workers=6)


class CIFAR10CIFAR100BYOL(SSLContainer):
    """
    This module trains an SSL encoder using BYOL on CIFAR10 and finetunes a linear head on CIFAR100.
    """

    def __init__(self) -> None:
        super().__init__(ssl_training_dataset_name=SSLDatasetName.CIFAR10,
                         classifier_dataset_name=SSLDatasetName.CIFAR100,
                         ssl_training_batch_size=512,
                         ssl_encoder=EncoderName.resnet50,
                         ssl_training_type=SSLType.BYOL,
                         random_seed=1,
                         recovery_checkpoint_save_interval=200,
                         num_epochs=2500,
                         num_workers=6)
