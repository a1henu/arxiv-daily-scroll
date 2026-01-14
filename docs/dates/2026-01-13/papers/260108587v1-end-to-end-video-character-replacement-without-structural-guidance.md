---
layout: default
title: End-to-End Video Character Replacement without Structural Guidance
---

# End-to-End Video Character Replacement without Structural Guidance
**arXiv**：[2601.08587v1](https://arxiv.org/abs/2601.08587) · [PDF](https://arxiv.org/pdf/2601.08587.pdf)  
**作者**：Zhengbo Xu, Jie Ma, Ziheng Wang, Zhan Peng, Jun Liang, Jing Li  

**一句话要点**：提出MoCha框架，仅需单帧掩码实现端到端视频角色替换，无需结构引导

**关键词**：视频角色替换, 端到端生成, 条件感知RoPE, RL后训练, 多模态数据集构建, 时序一致性

## 3 点简述
- 核心问题：现有方法依赖逐帧分割掩码和结构引导，在遮挡、交互等复杂场景中泛化性差
- 方法要点：引入条件感知RoPE和RL后训练阶段，构建三种专用数据集解决配对数据稀缺问题
- 实验效果：在复杂场景下显著优于现有方法，减少视觉伪影并提升时序一致性

## 摘要（原文）

> Controllable video character replacement with a user-provided identity remains a challenging problem due to the lack of paired video data. Prior works have predominantly relied on a reconstruction-based paradigm that requires per-frame segmentation masks and explicit structural guidance (e.g., skeleton, depth). This reliance, however, severely limits their generalizability in complex scenarios involving occlusions, character-object interactions, unusual poses, or challenging illumination, often leading to visual artifacts and temporal inconsistencies. In this paper, we propose MoCha, a pioneering framework that bypasses these limitations by requiring only a single arbitrary frame mask. To effectively adapt the multi-modal input condition and enhance facial identity, we introduce a condition-aware RoPE and employ an RL-based post-training stage. Furthermore, to overcome the scarcity of qualified paired-training data, we propose a comprehensive data construction pipeline. Specifically, we design three specialized datasets: a high-fidelity rendered dataset built with Unreal Engine 5 (UE5), an expression-driven dataset synthesized by current portrait animation techniques, and an augmented dataset derived from existing video-mask pairs. Extensive experiments demonstrate that our method substantially outperforms existing state-of-the-art approaches. We will release the code to facilitate further research. Please refer to our project page for more details: orange-3dv-team.github.io/MoCha

