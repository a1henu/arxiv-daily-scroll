---
layout: default
title: Towards autonomous time-calibration of large quantum-dot devices: Detection, real-time feedback, and noise spectroscopy
---

# Towards autonomous time-calibration of large quantum-dot devices: Detection, real-time feedback, and noise spectroscopy
**arXiv**：[2512.24894v1](https://arxiv.org/abs/2512.24894) · [PDF](https://arxiv.org/pdf/2512.24894.pdf)  
**作者**：Anantha S. Rao, Barnaby van Straaten, Valentin John, Cécile X. Yu, Stefan D. Oosterhout, Lucas Stehouwer, Giordano Scappucci, M. D. Stewart,, Menno Veldhorst, Francesco Borsoi, Justyna P. Zwolak  

**一句话要点**：提出基于电荷稳定性图自主校准方法，以解决量子点设备静电漂移问题，实现稳定操作与噪声分析。

**关键词**：量子点校准, 静电漂移检测, 实时反馈控制, 噪声谱分析, 电荷稳定性图, 自主系统

## 3 点简述
- 核心问题：半导体量子点比特受静电漂移和电荷噪声影响，导致操作点偏移，限制性能与可扩展性。
- 方法要点：利用电荷稳定性图中的电荷跃迁线网络作为多维探针，实时跟踪漂移并应用补偿更新。
- 实验或效果：在10量子点设备上演示稳定操作，实现噪声谱分析和空间相关性测量，支持自主校准模块。

## 摘要（原文）

> The performance and scalability of semiconductor quantum-dot (QD) qubits are limited by electrostatic drift and charge noise that shift operating points and destabilize qubit parameters. As systems expand to large one- and two-dimensional arrays, manual recalibration becomes impractical, creating a need for autonomous stabilization frameworks. Here, we introduce a method that uses the full network of charge-transition lines in repeatedly acquired double-quantum-dot charge stability diagrams (CSDs) as a multidimensional probe of the local electrostatic environment. By accurately tracking the motion of selected transitions in time, we detect voltage drifts, identify abrupt charge reconfigurations, and apply compensating updates to maintain stable operating conditions. We demonstrate our approach on a 10-QD device, showing robust stabilization and real-time diagnostic access to dot-specific noise processes. The high acquisition rate of radio-frequency reflectometry CSD measurements also enables time-domain noise spectroscopy, allowing the extraction of noise power spectral densities, the identification of two-level fluctuators, and the analysis of spatial noise correlations across the array. From our analysis, we find that the background noise at 100~$μ$\si{\hertz} is dominated by drift with a power law of $1/f^2$, accompanied by a few dominant two-level fluctuators and an average linear correlation length of $(188 \pm 38)$~\si{\nano\meter} in the device. These capabilities form the basis of a scalable, autonomous calibration and characterization module for QD-based quantum processors, providing essential feedback for long-duration, high-fidelity qubit operations.

