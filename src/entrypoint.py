from src.helpers.argument_input import parse_inputs
from src.helpers.turing_machine import TuringMachineSimulator
from src.ktape_dtm import KTape_DTM
from src.ntm_tracer import NTM_Tracer
from src.tm_reset_esotka import TM_RESET


def main():
    """
    Entry point for the project1_toc package.
    """

    args = parse_inputs()
    temp_sim = TuringMachineSimulator(args.file)

    # Assumes test for program 3, reset TM
    tmReset = TM_RESET(args.file)
    tmReset.run(args.input_string, args.max_depth)