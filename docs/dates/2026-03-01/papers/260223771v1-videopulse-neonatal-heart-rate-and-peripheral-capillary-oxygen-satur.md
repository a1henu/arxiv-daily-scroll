---
layout: default
title: VideoPulse: Neonatal heart rate and peripheral capillary oxygen saturation (SpO2) estimation from contact free video
---

# VideoPulse: Neonatal heart rate and peripheral capillary oxygen saturation (SpO2) estimation from contact free video
**arXiv**：[2602.23771v1](https://arxiv.org/abs/2602.23771) · [PDF](https://arxiv.org/pdf/2602.23771.pdf)  
**作者**：Deependra Dewagiri, Kamesh Anuradha, Pabadhi Liyanage, Helitha Kulatunga, Pamuditha Somarathne, Udaya S. K. P. Miriya Thanthrige, Nishani Lucas, Anusha Withana, Joshua P. Kulasingham  

**一句话要点**：提出VideoPulse数据集与端到端流程，通过非接触式视频估计新生儿心率和血氧饱和度。

**关键词**：远程光电容积描记术, 新生儿监测, 非接触式视频分析, 3D卷积神经网络, 生命体征估计, 数据集构建

## 3 点简述
- 核心问题：传统新生儿生命体征监测需皮肤接触，易致刺激和感染风险，需非侵入式方法。
- 方法要点：使用远程光电容积描记术，结合人脸对齐、去噪监督和3D CNN回归，支持短时窗口预测。
- 实验或效果：在NBHR数据集上，心率MAE为2.97 bpm，血氧饱和度MAE为1.69%，跨数据集评估显示良好泛化能力。

## 摘要（原文）

> Remote photoplethysmography (rPPG) enables contact free monitoring of vital signs and is especially valuable for neonates, since conventional methods often require sustained skin contact with adhesive probes that can irritate fragile skin and increase infection control burden. We present VideoPulse, a neonatal dataset and an end to end pipeline that estimates neonatal heart rate and peripheral capillary oxygen saturation (SpO2) from facial video. VideoPulse contains 157 recordings totaling 2.6 hours from 52 neonates with diverse face orientations. Our pipeline performs face alignment and artifact aware supervision using denoised pulse oximeter signals, then applies 3D CNN backbones for heart rate and SpO2 regression with label distribution smoothing and weighted regression for SpO2. Predictions are produced in 2 second windows. On the NBHR neonatal dataset, we obtain heart rate MAE 2.97 bpm using 2 second windows (2.80 bpm at 6 second windows) and SpO2 MAE 1.69 percent. Under cross dataset evaluation, the NBHR trained heart rate model attains 5.34 bpm MAE on VideoPulse, and fine tuning an NBHR pretrained SpO2 model on VideoPulse yields MAE 1.68 percent. These results indicate that short unaligned neonatal video segments can support accurate heart rate and SpO2 estimation, enabling low cost non invasive monitoring in neonatal intensive care.

