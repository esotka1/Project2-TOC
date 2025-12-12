from src.helpers.turing_machine import TuringMachineSimulator

BLANK = "_"
DIR_L = "L"
DIR_R = "R"

# ==========================================
# PROGRAM 3:RESET TM [cite: 268]
# ==========================================
class TM_RESET(TuringMachineSimulator):
    def run(self, input_string, max_steps):
        """
        Simulates a machine that resets on left instruction.
        """
        print(f"Running RESET TM (Single Tape): {self.machine_name}")

        # Initialization of TM variables
        current_state = self.start_state
        tape = list(input_string) if input_string else [BLANK]
        head = 0
        step = 0

        # Loop of TM steps
        while step < max_steps:

            # Ensures always a place for head to go
            if head >= len(tape):
                tape.append(BLANK)

            # Creates tape variable
            tape_display = ""
            for i, c in enumerate(tape):
                if i == head:
                    tape_display += f"[{c}]"
                else:
                    tape_display += f" {c} "

            # Displays TM info by step
            print(f"\nStep: {step}")
            print(f"State: {current_state}")
            print(f"Tape: {tape_display}")

            # Performs the transition for TM if possible
            transitions = self.get_transitions(current_state, tape[head])
            if not transitions:
                print(f"\nREJECT (No transition)\nFinal Tape: {''.join(tape)}")
                return False

            trans = transitions[0]
            next_state = trans['next']
            write_char = trans['write'][0]
            move_dir = trans['move'][0]
            tape[head] = write_char

            # Move head of TM
            if move_dir == DIR_L:
                head = 0
            elif move_dir == DIR_R:
                head += 1

            # Updates State / Steps taken
            current_state = next_state
            step += 1

            # Breaks out of loop if in final state
            if current_state == self.accept_state or current_state == self.reject_state:
                break

        # Display final answer
        if current_state == self.accept_state:
            print(f"\nACCEPT\nFinal Tape: {''.join(tape)}")
            return True
        elif current_state == self.reject_state:
            print(f"\nREJECT\nFinal Tape: {''.join(tape)}")
            return False
        else:
            print(f"\nMax Steps {max_steps} Reached")
            return False
