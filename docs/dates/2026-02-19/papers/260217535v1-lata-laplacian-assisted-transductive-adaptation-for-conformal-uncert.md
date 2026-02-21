---
layout: default
title: LATA: Laplacian-Assisted Transductive Adaptation for Conformal Uncertainty in Medical VLMs
---

# LATA: Laplacian-Assisted Transductive Adaptation for Conformal Uncertainty in Medical VLMs
**arXiv**：[2602.17535v1](https://arxiv.org/abs/2602.17535) · [PDF](https://arxiv.org/pdf/2602.17535.pdf)  
**作者**：Behzad Bozorgtabar, Dwarikanath Mahapatra, Sudipta Roy, Muzammal Naseer, Imran Razzak, Zongyuan Ge  

**一句话要点**：提出LATA方法，通过拉普拉斯辅助转导适应改进医学视觉语言模型在域移下的不确定性校准。

**关键词**：医学视觉语言模型, 不确定性校准, 转导适应, 保形预测, 拉普拉斯平滑, 零样本识别

## 3 点简述
- 医学视觉语言模型在零样本识别中面临域移下不确定性校准不可靠的问题，导致预测集过大和类别覆盖不平衡。
- LATA采用训练和标签无关的转导适应，基于图像-图像k-NN图平滑零样本概率，保持保形预测有效性，并引入失败感知分数提升效率。
- 在三个医学视觉语言模型和九个下游任务中，LATA一致减少预测集大小和类别覆盖差距，匹配或收紧目标覆盖，优于基线方法。

## 摘要（原文）

> Medical vision-language models (VLMs) are strong zero-shot recognizers for medical imaging, but their reliability under domain shift hinges on calibrated uncertainty with guarantees. Split conformal prediction (SCP) offers finite-sample coverage, yet prediction sets often become large (low efficiency) and class-wise coverage unbalanced-high class-conditioned coverage gap (CCV), especially in few-shot, imbalanced regimes; moreover, naively adapting to calibration labels breaks exchangeability and voids guarantees. We propose \texttt{\textbf{LATA}} (Laplacian-Assisted Transductive Adaptation), a \textit{training- and label-free} refinement that operates on the joint calibration and test pool by smoothing zero-shot probabilities over an image-image k-NN graph using a small number of CCCP mean-field updates, preserving SCP validity via a deterministic transform. We further introduce a \textit{failure-aware} conformal score that plugs into the vision-language uncertainty (ViLU) framework, providing instance-level difficulty and label plausibility to improve prediction set efficiency and class-wise balance at fixed coverage. \texttt{\textbf{LATA}} is black-box (no VLM updates), compute-light (windowed transduction, no backprop), and includes an optional prior knob that can run strictly label-free or, if desired, in a label-informed variant using calibration marginals once. Across \textbf{three} medical VLMs and \textbf{nine} downstream tasks, \texttt{\textbf{LATA}} consistently reduces set size and CCV while matching or tightening target coverage, outperforming prior transductive baselines and narrowing the gap to label-using methods, while using far less compute. Comprehensive ablations and qualitative analyses show that \texttt{\textbf{LATA}} sharpens zero-shot predictions without compromising exchangeability.

