# Hand Gesture Recognition for Smart Home Control

**Computer Vision · MediaPipe · OpenCV · Python · Arduino Mega 2560 · Zigbee · Modbus RTU**

Undergraduate capstone project (2023), Vietnam Aviation Academy (Faculty of Electronics). Developed by **Nguyen Quynh Trang** and **Dinh Thi Phuong Thao**, supervised by **Dr. Tran Quoc Khai**.

> **Project provenance:** This repository is a portfolio-ready documentation and simulation package based on our 2023 thesis. The verified original Python program is linked below. The hardware controller firmware and complete project Drive assets have not yet been supplied here. The `src/` simulator is a **new demonstration**, not claimed to be the original implementation.

## Overview

A webcam detects hand landmarks using MediaPipe, converts finger states to digits (0–5), collects a 3-digit device command, then transmits it over serial / Zigbee to an Arduino Mega 2560 controller. The Arduino communicates with Modbus relay modules through a TTL-to-RS485 interface to switch household appliances. A return code `1111` indicates success and `1110` indicates failure in the documented workflow.

![Thesis system block diagram](assets/system_block_diagram.png)

## Original project architecture

```text
Camera → Python/OpenCV → MediaPipe hand landmarks → finger-state recognition
    → digit sequence (three-digit command) → serial → XBee/Zigbee
    → Arduino Mega 2560 → TTL/RS485 → Modbus RTU relay → appliance
                                      ↳ ACK 1111 / NACK 1110
```

## Documented command mapping

| Code ON | Code OFF | Controlled appliances |
| --- | --- | --- |
| 100 | 105 | Floor 1 lights & fan |
| 110 | 115 | Floor 1 television & fan |
| 200 | 205 | Floor 2 television |
| 210 | 215 | Floor 2 lights & fan |
| 300 | **305\*** | Floor 3 lights & fan |
| 310 | 315 | Garden lights & fan |
| 000 | 005 | Garage gate |
| 550 | 555 | All devices |

\* **Source inconsistency:** Table 5 in the thesis lists `205` as the OFF command for floor 3, which conflicts with the displayed `30-` family and the 0/5 command convention. The simulator uses inferred `305`, **not a verified original command**; confirm against the actual Arduino firmware before controlling physical equipment.

## Included in this repository

- The thesis is not bundled for public posting because it includes student IDs and co-author material; add a redacted copy only after obtaining permission.
- `assets/` — system architecture illustration extracted from the thesis (review publication rights before uploading).
- `src/commands.py` — documented command reference and validation, with the above caveat.
- `src/simulator.py` — safe software-only appliance state simulator.
- `tests/` — automated unit tests for simulator.
- `original/SOURCE.md` — link to the original 2023 Python source.

## Run the software-only demo (no hardware, no camera required)

```bash
python -m src.simulator 100 105 000 005 550 555
python -m unittest discover -s tests -v
```

**The software-only demo is not a reproduction of the original camera recognition or Zigbee/Arduino control path.** For the original camera application, consult [handsignature_v7.py](https://github.com/mysuachua/Luanvan/blob/main/handsignature_v7.py). It uses OpenCV, MediaPipe and pyserial, and assumes a Windows `COM6` serial connection; do not run with hardware attached without reviewing settings and validating safe relay behavior.

## Results and limitations

Chapter 4 documents ON/OFF demonstration figures for appliance groups. The thesis qualitatively reports successful operation but **does not provide a reproducible quantitative benchmark, dataset, accuracy %, latency distribution, or public test logs**. No numerical metric is claimed in this repository.

Known limitations: lighting, occlusion, hand orientation, stable gesture recognition, serial device configuration, and lack of full published firmware / measurements. The original implementation includes a 10-frame averaging step and parses `1111` / `1110` feedback.

## Attribution and rights

This project was completed jointly by Nguyen Quynh Trang and Dinh Thi Phuong Thao, under Dr. Tran Quoc Khai. Credit for the original source is retained at the linked repository. No license for the original 2023 source is asserted here. Confirm collaborator agreement before republishing third-party media or proprietary source.

## Suggested next steps

1. Supply the Drive folder URL or original files (Arduino firmware, wiring diagram, photos/videos, experiment logs).
2. Validate all device codes against actual firmware, particularly `300/305`.
3. Separate PC and Arduino components, add a hardware-free transport mock and hardware integration instructions.
4. Add an annotated video demo, measured evaluation and safety precautions.

## CV line

**Hand Gesture Recognition for Smart Home Control (Capstone, 2023)** — Co-developed a computer-vision-based smart home control system integrating MediaPipe/OpenCV gesture recognition with Zigbee, Arduino Mega 2560, and Modbus RTU relay control; documented and demonstrated appliance ON/OFF scenarios.


## Verified original project materials (2023)

The shared Google Drive folder includes a recorded graduation-project demo, an edited demo, a dated student work log, and a MediaPipe/OpenCV notebook. See [Drive source inventory](docs/DRIVE_SOURCES.md). The notebook is retained under [`notebooks/HAND_NUMBER_original_clean.ipynb`](notebooks/HAND_NUMBER_original_clean.ipynb) with execution outputs removed.

**Provenance:** The original thesis work was jointly completed by Nguyen Quynh Trang and Dinh Thi Phuong Thao, supervised by Dr. Tran Quoc Khai. The Python simulator in `src/` is a newly written illustrative companion; it is **not** the 2023 physical control firmware. The original notebook may require older MediaPipe versions, webcam hardware, and environment adjustments to run. Original video links point to Google Drive and are not embedded or reproduced here.
