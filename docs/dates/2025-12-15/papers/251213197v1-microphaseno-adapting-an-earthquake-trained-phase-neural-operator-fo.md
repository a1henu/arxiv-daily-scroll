---
layout: default
title: MicroPhaseNO: Adapting an Earthquake-Trained Phase Neural Operator for Microseismic Phase Picking
---

# MicroPhaseNO: Adapting an Earthquake-Trained Phase Neural Operator for Microseismic Phase Picking
**arXiv**：[2512.13197v1](https://arxiv.org/abs/2512.13197) · [PDF](https://arxiv.org/pdf/2512.13197.pdf)  
**作者**：Ayrat Abdullin, Umair bin Waheed, Leo Eisner, Naveed Iqbal  

**一句话要点**：提出MicroPhaseNO，通过迁移学习将地震相位神经算子适配于微地震相位拾取

**关键词**：微地震监测, 相位拾取, 迁移学习, 神经算子, 地震数据处理, 深度学习

## 3 点简述
- 核心问题：传统地震相位拾取器在微地震数据上性能不佳，因微地震信号噪声高、网络时间短且标注方式不同。
- 方法要点：基于预训练的PhaseNO模型，仅用200个微地震记录进行微调，保留地震数据学习到的时空表示，适应微地震特征。
- 实验或效果：在三个真实微地震数据集上评估，F1分数和准确率提升高达30%，显著减少时间偏差和拾取不确定性。

## 摘要（原文）

> Seismic phase picking is very often used for microseismic monitoring and subsurface imaging. Traditional manual processing is not feasible for either real-time applications or large arrays. Deep learning-based pickers trained on large earthquake catalogs offer an automated alternative. However, they are typically optimized for high signal-to-noise, long-duration networks and struggle with the challenges presented by microseismic datasets, which are purpose-built for limited time without previously detected seismicity. In this study, we demonstrate how a network-wide earthquake phase picker, the Phase Neural Operator (PhaseNO), can be adapted to microseismic monitoring using transfer learning. Starting from a PhaseNO model pre-trained on more than 57,000 three-component earthquake and noise records, we fine-tune the model using only 200 labeled and noise seismograms from induced events in hydraulic-fracturing settings. The fine-tuned model thus preserves the rich spatio-temporal representation learned from abundant earthquake data, while adapting to the characteristics and labeling conventions of microseismic phases, which are often picked on peaks or troughs rather than onsets. We evaluate performance on three distinct real-world microseismic datasets with different network geometries and acquisition parameters. Compared to the original PhaseNO and a conventional workflow, the adapted model increases F1 score and accuracy by up to 30%, and strongly reduces systematic timing bias and pick uncertainty. Because the adaptation relies on a small, campaign-specific calibration set, the approach is readily transferable to other microseismic tasks where public earthquake data and pre-trained models are accessible. The associated code will be released openly at https://github.com/ayratabd/MicroPhaseNO.

