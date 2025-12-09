---
layout: default
title: Debiasing Diffusion Priors via 3D Attention for Consistent Gaussian Splatting
---

# Debiasing Diffusion Priors via 3D Attention for Consistent Gaussian Splatting
**arXiv**：[2512.07345v1](https://arxiv.org/abs/2512.07345) · [PDF](https://arxiv.org/pdf/2512.07345.pdf)  
**作者**：Shilong Jin, Haoran Duan, Litao Hua, Wentao Huang, Yuan Zhou  

**一句话要点**：提出TD-Attn框架，通过3D注意力机制解决文本到图像扩散模型在3D任务中的多视角不一致问题。

**关键词**：3D生成, 扩散模型, 多视角一致性, 注意力机制, 文本到图像, 高斯溅射

## 3 点简述
- 核心问题：文本到图像扩散模型存在先验视角偏差，导致3D任务中不同视角外观冲突。
- 方法要点：引入3D-AAG模块构建视图一致的3D注意力高斯，HAM模块通过语义引导树调制跨注意力层。
- 实验或效果：TD-Attn作为通用插件，显著提升3D任务的多视角一致性，支持可控编辑。

## 摘要（原文）

> Versatile 3D tasks (e.g., generation or editing) that distill from Text-to-Image (T2I) diffusion models have attracted significant research interest for not relying on extensive 3D training data. However, T2I models exhibit limitations resulting from prior view bias, which produces conflicting appearances between different views of an object. This bias causes subject-words to preferentially activate prior view features during cross-attention (CA) computation, regardless of the target view condition. To overcome this limitation, we conduct a comprehensive mathematical analysis to reveal the root cause of the prior view bias in T2I models. Moreover, we find different UNet layers show different effects of prior view in CA. Therefore, we propose a novel framework, TD-Attn, which addresses multi-view inconsistency via two key components: (1) the 3D-Aware Attention Guidance Module (3D-AAG) constructs a view-consistent 3D attention Gaussian for subject-words to enforce spatial consistency across attention-focused regions, thereby compensating for the limited spatial information in 2D individual view CA maps; (2) the Hierarchical Attention Modulation Module (HAM) utilizes a Semantic Guidance Tree (SGT) to direct the Semantic Response Profiler (SRP) in localizing and modulating CA layers that are highly responsive to view conditions, where the enhanced CA maps further support the construction of more consistent 3D attention Gaussians. Notably, HAM facilitates semantic-specific interventions, enabling controllable and precise 3D editing. Extensive experiments firmly establish that TD-Attn has the potential to serve as a universal plugin, significantly enhancing multi-view consistency across 3D tasks.

