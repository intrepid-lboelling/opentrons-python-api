#!/usr/bin/env python

from typing import Optional
from ot_api.decorators import command, request_with_run_id
import ot_api.requestor
import ot_api.runs



def list_connected_modules():
    """List the connected modules"""
    return ot_api.requestor.get('/modules')['data']

@command
def load_module(
    model: str, 
    slot: int,
    moduleId: Optional[str] = None,
    run_id: Optional[str] = None,
):
    assert slot in range(1, 13)
    params = {
        "model": model,
        "location": {
            "slotName": str(slot),
        },
        "moduleId": moduleId,
    }

    ot_api.runs.enqueue_command(
        "loadModule", params=params, intent="setup", run_id=run_id
    )


@command
def open_labware_latch(
    module_id: str,
    run_id: Optional[str] = None,
):
    params = {"moduleId": module_id}
    return ot_api.runs.enqueue_command(
        "heaterShaker/openLabwareLatch",
        params,
        intent="setup",
        run_id=run_id,
    )


@command
def close_labware_latch(
    module_id: str,
    run_id: Optional[str] = None,
):
    params = {"moduleId": module_id}
    return ot_api.runs.enqueue_command(
        "heaterShaker/closeLabwareLatch",
        params,
        intent="setup",
        run_id=run_id,
    )


@command
def wait_for_temperature(
    module_id: str,
    temp: float,  # target temp in deg C
    run_id: Optional[str] = None,
):
    params = {
        "moduleId": module_id,
        "celsius": temp,
    }
    return ot_api.runs.enqueue_command(
        "heaterShaker/waitForTemperature", params, intent="setup", run_id=run_id
    )


@command
def set_target_temperature(
    module_id: str,
    temp: float,  # target temp in deg C
    run_id: Optional[str] = None,
):
    params = {
        "moduleId": module_id,
        "celsius": temp,
    }
    return ot_api.runs.enqueue_command(
        "heaterShaker/setTargetTemperature", params, intent="setup", run_id=run_id
    )


@command
def deactivate_heater(
    module_id: str,
    run_id: Optional[str] = None,
):
    params = {
        "moduleId": module_id,
    }
    return ot_api.runs.enqueue_command(
        "heaterShaker/deactivateHeater", params, intent="setup", run_id=run_id
    )


@command
def set_wait_shake_speed(
    module_id: str,
    rpm: float,  # target speed in rotations per minute
    run_id: Optional[str] = None,
):
    assert 200.0 <= rpm <= 3000.0
    params = {
        "moduleId": module_id,
        "rpm": rpm,
    }
    return ot_api.runs.enqueue_command(
        "heaterShaker/setAndWaitForShakeSpeed",
        params,
        intent="setup",
        run_id=run_id,
    )


@command
def deactivate_shaker(
    module_id: str,
    run_id: Optional[str] = None,
):
    params = {"moduleId": module_id}
    return ot_api.runs.enqueue_command(
        "heaterShaker/deactivateShaker",
        params,
        intent="setup",
        run_id=run_id,
    )