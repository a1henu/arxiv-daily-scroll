---
layout: default
title: Beyond Language Modeling: An Exploration of Multimodal Pretraining
---

# Beyond Language Modeling: An Exploration of Multimodal Pretraining
**arXiv**：[2603.03276v1](https://arxiv.org/abs/2603.03276) · [PDF](https://arxiv.org/pdf/2603.03276.pdf)  
**作者**：Shengbang Tong, David Fan, John Nguyen, Ellis Brown, Gaoyue Zhou, Shengyi Qian, Boyang Zheng, Théophane Vallaeys, Junlin Han, Rob Fergus, Naila Murray, Marjan Ghazvininejad, Mike Lewis, Nicolas Ballas, Amir Bar, Michael Rabbat, Jakob Verbeek, Luke Zettlemoyer, Koustuv Sinha, Yann LeCun, Saining Xie  

**一句话要点**：提出Transfusion框架探索原生多模态预训练，揭示视觉与语言协同及缩放不对称性

**关键词**：多模态预训练, Transfusion框架, 表示自编码器, 缩放不对称性, 专家混合模型, 世界建模

## 3 点简述
- 核心问题：原生多模态模型设计空间不透明，需隔离语言预训练干扰以明确因素。
- 方法要点：采用Transfusion框架，结合语言的下一个词预测和视觉的扩散模型，训练于文本、视频等多源数据。
- 实验或效果：发现RAE为最优统一视觉表示，视觉与语言数据互补，MoE架构高效处理缩放不对称性。

## 摘要（原文）

> The visual world offers a critical axis for advancing foundation models beyond language. Despite growing interest in this direction, the design space for native multimodal models remains opaque. We provide empirical clarity through controlled, from-scratch pretraining experiments, isolating the factors that govern multimodal pretraining without interference from language pretraining. We adopt the Transfusion framework, using next-token prediction for language and diffusion for vision, to train on diverse data including text, video, image-text pairs, and even action-conditioned video. Our experiments yield four key insights: (i) Representation Autoencoder (RAE) provides an optimal unified visual representation by excelling at both visual understanding and generation; (ii) visual and language data are complementary and yield synergy for downstream capabilities; (iii) unified multimodal pretraining leads naturally to world modeling, with capabilities emerging from general training; and (iv) Mixture-of-Experts (MoE) enables efficient and effective multimodal scaling while naturally inducing modality specialization. Through IsoFLOP analysis, we compute scaling laws for both modalities and uncover a scaling asymmetry: vision is significantly more data-hungry than language. We demonstrate that the MoE architecture harmonizes this scaling asymmetry by providing the high model capacity required by language while accommodating the data-intensive nature of vision, paving the way for truly unified multimodal models.

