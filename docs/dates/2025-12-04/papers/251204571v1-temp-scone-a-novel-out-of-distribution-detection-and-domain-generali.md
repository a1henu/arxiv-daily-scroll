---
layout: default
title: Temp-SCONE: A Novel Out-of-Distribution Detection and Domain Generalization Framework for Wild Data with Temporal Shift
---

# Temp-SCONE: A Novel Out-of-Distribution Detection and Domain Generalization Framework for Wild Data with Temporal Shift
**arXiv**：[2512.04571v1](https://arxiv.org/abs/2512.04571) · [PDF](https://arxiv.org/pdf/2512.04571.pdf)  
**作者**：Aditi Naiknaware, Sanchit Singh, Hajar Homayouni, Salimeh Sekeh  

**一句话要点**：提出Temp-SCONE以处理动态环境中时间漂移的OOD检测与域泛化问题

**关键词**：时间漂移处理, OOD检测, 域泛化, 置信度正则化, 动态环境学习

## 3 点简述
- 核心问题：现有方法如SCONE在静态环境中鲁棒，但在动态域中性能下降，需处理时间漂移
- 方法要点：基于ATC引入置信度驱动正则化损失，惩罚时间步间预测不稳定性，保持能量边界分离
- 实验或效果：在动态数据集上显著提升时间漂移下的鲁棒性，OOD检测更可靠，非连续数据集性能相当

## 摘要（原文）

> Open-world learning (OWL) requires models that can adapt to evolving environments while reliably detecting out-of-distribution (OOD) inputs. Existing approaches, such as SCONE, achieve robustness to covariate and semantic shifts but assume static environments, leading to degraded performance in dynamic domains. In this paper, we propose Temp-SCONE, a temporally consistent extension of SCONE designed to handle temporal shifts in dynamic environments. Temp-SCONE introduces a confidence-driven regularization loss based on Average Thresholded Confidence (ATC), penalizing instability in predictions across time steps while preserving SCONE's energy-margin separation. Experiments on dynamic datasets demonstrate that Temp-SCONE significantly improves robustness under temporal drift, yielding higher corrupted-data accuracy and more reliable OOD detection compared to SCONE. On distinct datasets without temporal continuity, Temp-SCONE maintains comparable performance, highlighting the importance and limitations of temporal regularization. Our theoretical insights on temporal stability and generalization error further establish Temp-SCONE as a step toward reliable OWL in evolving dynamic environments.

