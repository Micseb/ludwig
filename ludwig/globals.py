#! /usr/bin/env python
# coding=utf-8
# Copyright 2019 The Ludwig Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
LUDWIG_VERSION = '0.23.3-dev0'

MODEL_WEIGHTS_FILE_NAME = 'model_weights'
MODEL_WEIGHTS_PROGRESS_FILE_NAME = 'model_weights_progress'
MODEL_HYPERPARAMETERS_FILE_NAME = 'model_hyperparameters.json'
TRAINING_PROGRESS_FILE_NAME = 'training_progress.p'

DISABLE_PROGRESSBAR = False


def set_disable_progressbar(value):
    global DISABLE_PROGRESSBAR
    DISABLE_PROGRESSBAR = value


def get_disable_progressbar():
    return DISABLE_PROGRESSBAR