---
layout: default
title: Deepfake Forensics Adapter: A Dual-Stream Network for Generalizable Deepfake Detection
---

# Deepfake Forensics Adapter: A Dual-Stream Network for Generalizable Deepfake Detection
**arXiv**：[2603.01450v1](https://arxiv.org/abs/2603.01450) · [PDF](https://arxiv.org/pdf/2603.01450.pdf)  
**作者**：Jianfeng Liao, Yichen Wei, Raymond Chan Ching Bon, Shulan Wang, Kam-Pui Chow, Kwok-Yan Lam  

**一句话要点**：提出Deepfake Forensics Adapter，一种双流网络，通过结合视觉语言基础模型与针对性取证分析，提升深度伪造检测的泛化能力。

**关键词**：深度伪造检测, 双流网络, 视觉语言模型, 泛化能力, 取证分析, CLIP适配器

## 3 点简述
- 核心问题：现有深度伪造检测方法在泛化到新兴伪造模式时存在局限性，难以应对快速发展的生成技术威胁。
- 方法要点：基于预训练CLIP模型，引入全局特征适配器、局部异常流和交互式融合分类器，在不改变CLIP参数的情况下实现针对性检测。
- 实验或效果：在DFDC等基准测试中取得先进性能，视频级AUC提升4.8%，展示了优越的泛化能力。

## 摘要（原文）

> The rapid advancement of deepfake generation techniques poses significant threats to public safety and causes societal harm through the creation of highly realistic synthetic facial media. While existing detection methods demonstrate limitations in generalizing to emerging forgery patterns, this paper presents Deepfake Forensics Adapter (DFA), a novel dual-stream framework that synergizes vision-language foundation models with targeted forensics analysis. Our approach integrates a pre-trained CLIP model with three core components to achieve specialized deepfake detection by leveraging the powerful general capabilities of CLIP without changing CLIP parameters: 1) A Global Feature Adapter is used to identify global inconsistencies in image content that may indicate forgery, 2) A Local Anomaly Stream enhances the model's ability to perceive local facial forgery cues by explicitly leveraging facial structure priors, and 3) An Interactive Fusion Classifier promotes deep interaction and fusion between global and local features using a transformer encoder. Extensive evaluations of frame-level and video-level benchmarks demonstrate the superior generalization capabilities of DFA, particularly achieving state-of-the-art performance in the challenging DFDC dataset with frame-level AUC/EER of 0.816/0.256 and video-level AUC/EER of 0.836/0.251, representing a 4.8% video AUC improvement over previous methods. Our framework not only demonstrates state-of-the-art performance, but also points out a feasible and effective direction for developing a robust deepfake detection system with enhanced generalization capabilities against the evolving deepfake threats. Our code is available at https://github.com/Liao330/DFA.git

