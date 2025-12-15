---
layout: default
title: Spectral entropy prior-guided deep feature fusion architecture for magnetic core loss
---

# Spectral entropy prior-guided deep feature fusion architecture for magnetic core loss
**arXiv**：[2512.11334v1](https://arxiv.org/abs/2512.11334) · [PDF](https://arxiv.org/pdf/2512.11334.pdf)  
**作者**：Cong Yao, Chunye Gong, Jin Zhang  

**一句话要点**：提出SEPI-TFPNet混合模型以提升磁芯损耗建模的准确性与鲁棒性

**关键词**：磁芯损耗建模, 混合模型, 谱熵先验, 特征融合, 深度学习, 电力电子

## 3 点简述
- 核心问题：传统磁芯损耗建模方法预测精度有限，纯数据驱动模型可解释性与跨分布泛化能力不足
- 方法要点：结合经验模型与深度学习，通过谱熵判别机制选择经验模型，并利用CNN、多头注意力和BiLSTM提取特征
- 实验或效果：在MagNet数据集上评估，相比2023年挑战赛21个模型及2024-2025年三个先进方法，建模精度和鲁棒性提升

## 摘要（原文）

> Accurate core loss modeling is critical for the design of high-efficiency power electronic systems. Traditional core loss modeling methods have limitations in prediction accuracy. To advance this field, the IEEE Power Electronics Society launched the MagNet Challenge in 2023, the first international competition focused on data-driven power electronics design methods, aiming to uncover complex loss patterns in magnetic components through a data-driven paradigm. Although purely data-driven models demonstrate strong fitting performance, their interpretability and cross-distribution generalization capabilities remain limited. To address these issues, this paper proposes a hybrid model, SEPI-TFPNet, which integrates empirical models with deep learning. The physical-prior submodule employs a spectral entropy discrimination mechanism to select the most suitable empirical model under different excitation waveforms. The data-driven submodule incorporates convolutional neural networks, multi-head attention mechanisms, and bidirectional long short-term memory networks to extract flux-density time-series features. An adaptive feature fusion module is introduced to improve multimodal feature interaction and integration. Using the MagNet dataset containing various magnetic materials, this paper evaluates the proposed method and compares it with 21 representative models from the 2023 challenge and three advanced methods from 2024-2025. The results show that the proposed method achieves improved modeling accuracy and robustness.

