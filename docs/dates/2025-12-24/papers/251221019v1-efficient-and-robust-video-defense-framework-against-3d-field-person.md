---
layout: default
title: Efficient and Robust Video Defense Framework against 3D-field Personalized Talking Face
---

# Efficient and Robust Video Defense Framework against 3D-field Personalized Talking Face
**arXiv**：[2512.21019v1](https://arxiv.org/abs/2512.21019) · [PDF](https://arxiv.org/pdf/2512.21019.pdf)  
**作者**：Rui-qing Sun, Xingshan Yao, Tian Lan, Hui-Yang Zhao, Jia-Ling Shi, Chen-Hao Cui, Zhijing Wu, Chen Yang, Xian-Ling Mao  

**一句话要点**：提出高效视频防御框架以保护肖像视频免受3D场说话人脸生成方法滥用

**关键词**：视频防御, 3D场说话人脸生成, 隐私保护, 参数共享, 双域扰动, 高保真视频

## 3 点简述
- 核心问题：现有3D场说话人脸生成方法可实时合成高保真个性化说话人脸视频，引发隐私泄露风险，但缺乏高效防御框架。
- 方法要点：通过扰动3D信息获取过程，引入相似性引导参数共享机制和多尺度双域注意力模块，以保持视频高保真度。
- 实验或效果：在实验中展现强防御能力，比最快基线加速47倍，并保持高保真度，对缩放操作和净化攻击具有鲁棒性。

## 摘要（原文）

> State-of-the-art 3D-field video-referenced Talking Face Generation (TFG) methods synthesize high-fidelity personalized talking-face videos in real time by modeling 3D geometry and appearance from reference portrait video. This capability raises significant privacy concerns regarding malicious misuse of personal portraits. However, no efficient defense framework exists to protect such videos against 3D-field TFG methods. While image-based defenses could apply per-frame 2D perturbations, they incur prohibitive computational costs, severe video quality degradation, failing to disrupt 3D information for video protection. To address this, we propose a novel and efficient video defense framework against 3D-field TFG methods, which protects portrait video by perturbing the 3D information acquisition process while maintain high-fidelity video quality. Specifically, our method introduces: (1) a similarity-guided parameter sharing mechanism for computational efficiency, and (2) a multi-scale dual-domain attention module to jointly optimize spatial-frequency perturbations. Extensive experiments demonstrate that our proposed framework exhibits strong defense capability and achieves a 47x acceleration over the fastest baseline while maintaining high fidelity. Moreover, it remains robust against scaling operations and state-of-the-art purification attacks, and the effectiveness of our design choices is further validated through ablation studies. Our project is available at https://github.com/Richen7418/VDF.

