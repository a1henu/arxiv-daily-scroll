---
layout: default
title: Performance Evaluation of an Integrated System for Visible Light Communication and Positioning Using an Event Camera
---

# Performance Evaluation of an Integrated System for Visible Light Communication and Positioning Using an Event Camera
**arXiv**：[2510.17203v1](https://arxiv.org/abs/2510.17203) · [PDF](https://arxiv.org/pdf/2510.17203.pdf)  
**作者**：Ryota Soga, Masataka Kobayashi, Tsukasa Shimizu, Shintaro Shiba, Quan Kong, Shan Lu, Takaya Yamazato  

**一句话要点**：提出集成事件相机的可见光通信与定位系统，用于GPS缺失环境下的车辆自定位。

**关键词**：事件相机, 可见光通信, 可见光定位, 车辆自定位, Walsh-Hadamard码, 相位相关

## 3 点简述
- 核心问题：车辆在GPS缺失环境（如隧道）中难以实现高精度自定位。
- 方法要点：使用事件相机结合Walsh-Hadamard码识别LED，实现VLC和VLP集成。
- 实验或效果：车辆以30 km/h行驶，距离估计RMSE≤0.75 m，BER<0.01。

## 摘要（原文）

> Event cameras, featuring high temporal resolution and high dynamic range,
> offer visual sensing capabilities comparable to conventional image sensors
> while capturing fast-moving objects and handling scenes with extreme lighting
> contrasts such as tunnel exits. Leveraging these properties, this study
> proposes a novel self-localization system that integrates visible light
> communication (VLC) and visible light positioning (VLP) within a single event
> camera. The system enables a vehicle to estimate its position even in
> GPS-denied environments, such as tunnels, by using VLC to obtain coordinate
> information from LED transmitters and VLP to estimate the distance to each
> transmitter.
>   Multiple LEDs are installed on the transmitter side, each assigned a unique
> pilot sequence based on Walsh-Hadamard codes. The event camera identifies
> individual LEDs within its field of view by correlating the received signal
> with these codes, allowing clear separation and recognition of each light
> source. This mechanism enables simultaneous high-capacity MISO (multi-input
> single-output) communication through VLC and precise distance estimation via
> phase-only correlation (POC) between multiple LED pairs.
>   To the best of our knowledge, this is the first vehicle-mounted system to
> achieve simultaneous VLC and VLP functionalities using a single event camera.
> Field experiments were conducted by mounting the system on a vehicle traveling
> at 30 km/h (8.3 m/s). The results demonstrated robust real-world performance,
> with a root mean square error (RMSE) of distance estimation within 0.75 m for
> ranges up to 100 m and a bit error rate (BER) below 0.01 across the same range.

