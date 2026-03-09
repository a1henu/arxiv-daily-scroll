---
layout: default
title: GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection
---

# GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection
**arXiv**：[2603.06048v1](https://arxiv.org/abs/2603.06048) · [PDF](https://arxiv.org/pdf/2603.06048.pdf)  
**作者**：Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  

**一句话要点**：提出GenHOI，通过时间平衡与空间选择性对象注入，提升手-物交互视频生成的对象一致性。

**关键词**：手-物交互生成, 视频编辑, 对象一致性, 时间平衡, 空间注意力, 野外场景泛化

## 3 点简述
- 核心问题：手-物交互视频生成中对象外观不一致，现有方法泛化能力不足。
- 方法要点：采用Head-Sliding RoPE实现时间平衡，设计两级空间注意力门增强空间选择性。
- 实验或效果：在未见野外场景评估中，显著优于先进的手-物交互重演和通用视频编辑方法。

## 摘要（原文）

> Hand-Object Interaction (HOI) remains a core challenge in digital human video synthesis, where models must generate physically plausible contact and preserve object identity across frames. Although recent HOI reenactment approaches have achieved progress, they are typically trained and evaluated in-domain and fail to generalize to complex, in-the-wild scenarios. In contrast, all-in-one video editing models exhibit broader robustness but still struggle with HOI-specific issues such as inconsistent object appearance. In this paper, we present GenHOI, a lightweight augmentation to pretrained video generation models that injects reference-object information in a temporally balanced and spatially selective manner. For temporal balancing, we propose Head-Sliding RoPE, which assigns head-specific temporal offsets to reference tokens, distributing their influence evenly across frames and mitigating the temporal decay of 3D RoPE to improve long-range object consistency. For spatial selectivity, we design a two-level spatial attention gate that concentrates object-conditioned attention on HOI regions and adaptively scales its strength, preserving background realism while enhancing interaction fidelity. Extensive qualitative and quantitative evaluations on unseen, in-the-wild scenes demonstrate that GenHOI significantly outperforms state-of-the-art HOI reenactment and all-in-one video editing methods. Project page: https://xuanhuang0.github.io/GenHOI/

