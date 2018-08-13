# Copyright 2017-2018 TensorHub, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division

import click

from guild import click_util
from . import runs_support

@click.command("info")
@runs_support.run_arg
@click.option("-e", "--env", help="Show run environment.", is_flag=True)
@click.option("-f", "--flags", help="Show run flags.", is_flag=True)
@click.option("-d", "--deps", help="Show resolved dependencies.", is_flag=True)
@click.option("-O", "--output", help="Show run output.", is_flag=True)
@click.option(
    "-p", "--page-output",
    help="Show only run output in a pager.",
    is_flag=True)
@click.option("-F", "--files", help="Show run files.", is_flag=True)
@click.option(
    "-L", "--follow-links",
    help="Follow links when showing files.",
    is_flag=True)
@click.option(
    "-A", "--all-files",
    help="Show all run files including those generated by Guild.",
    is_flag=True)
@click.option(
    "-P", "--full-path",
    help="Display full path when showing files.",
    is_flag=True)
@runs_support.op_and_label_filters
@runs_support.status_filters

@click.pass_context
@click_util.use_args
@click_util.render_doc

def run_info(ctx, args):
    """Show run information.

    This command shows information for a single run.

    {{ runs_support.run_arg }}

    If RUN isn't specified, the latest run is selected.

    ### Additional information

    You can show additional run information by specifying option
    flags. You may use multiple flags to show more information. Refer
    to the options below for what additional information is available.

    {{ runs_support.op_and_label_filters }}
    {{ runs_support.status_filters }}

    """
    from . import runs_impl
    runs_impl.run_info(args, ctx)
