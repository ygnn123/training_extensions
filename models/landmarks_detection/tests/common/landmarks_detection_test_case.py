# Copyright (C) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions
# and limitations under the License.

import os


from ote.tests.test_case import create_export_test_case, create_test_case
from ote.tests.utils import collect_ap
from ote.utils.misc import run_through_shell



def create_landmarks_detection_test_case(**kwargs):
    expected_outputs_dir = os.path.join(os.path.dirname(__file__), '..', 'expected_outputs')
    TestCase = create_test_case('landmarks-detection',
                                **kwargs,
                                metric_keys=['NME'],
                                expected_outputs_dir=expected_outputs_dir)

    class LandmarksDetectionTestCase(TestCase):

        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            wider_lms_dir = os.path.abspath(f'{os.path.dirname(__file__)}/../../../../data/wider_face_lms')

    return LandmarksDetectionTestCase


def create_landmarks_detection_export_test_case(**kwargs):
    expected_outputs_dir = os.path.join(os.path.dirname(__file__), '..', 'expected_outputs')
    ExportTestCase = create_export_test_case('landmarks_detection',
                                             **kwargs,
                                             metric_keys=['mAP'],
                                             expected_outputs_dir=expected_outputs_dir)

    class LandmarksDetectionExportTestCase(ExportTestCase):

        @classmethod
        def setUpClass(cls):
            super().setUpClass()
            wider_lms_dir = os.path.abspath(f'{os.path.dirname(__file__)}/../../../../data/wider_face_lms')

    return LandmarksDetectionExportTestCase
