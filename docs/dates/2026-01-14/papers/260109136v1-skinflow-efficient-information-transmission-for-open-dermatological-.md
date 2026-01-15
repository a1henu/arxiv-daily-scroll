---
layout: default
title: SkinFlow: Efficient Information Transmission for Open Dermatological Diagnosis via Dynamic Visual Encoding and Staged RL
---

# SkinFlow: Efficient Information Transmission for Open Dermatological Diagnosis via Dynamic Visual Encoding and Staged RL
**arXiv**：[2601.09136v1](https://arxiv.org/abs/2601.09136) · [PDF](https://arxiv.org/pdf/2601.09136.pdf)  
**作者**：Lijun Liu, Linwei Chen, Zhishou Zhang, Meng Tian, Hengfu Cui, Ruiyang Li, Zhaocheng Liu, Qiang Ju, Qianxi Li, Hong-Yu Zhou  

**一句话要点**：提出SkinFlow框架，通过动态视觉编码和分阶段强化学习优化皮肤病诊断中的视觉信息传输效率。

**关键词**：皮肤病诊断, 动态视觉编码, 强化学习, 信息传输优化, 医学视觉模型

## 3 点简述
- 核心问题：通用大视觉语言模型在皮肤病诊断中因注意力分散，难以区分细微病变与背景噪声。
- 方法要点：采用虚拟宽度动态视觉编码器展开复杂病理流形，结合两阶段强化学习策略，在受限语义空间内对齐显式医学描述和重建隐式诊断纹理。
- 实验或效果：在Fitzpatrick17k基准上，7B模型实现Top-1准确率提升12.06%，Top-6准确率提升28.57%，超越大规模通用模型。

## 摘要（原文）

> General-purpose Large Vision-Language Models (LVLMs), despite their massive scale, often falter in dermatology due to "diffuse attention" - the inability to disentangle subtle pathological lesions from background noise. In this paper, we challenge the assumption that parameter scaling is the only path to medical precision. We introduce SkinFlow, a framework that treats diagnosis as an optimization of visual information transmission efficiency. Our approach utilizes a Virtual-Width Dynamic Vision Encoder (DVE) to "unfold" complex pathological manifolds without physical parameter expansion, coupled with a two-stage Reinforcement Learning strategy. This strategy sequentially aligns explicit medical descriptions (Stage I) and reconstructs implicit diagnostic textures (Stage II) within a constrained semantic space. Furthermore, we propose a clinically grounded evaluation protocol that prioritizes diagnostic safety and hierarchical relevance over rigid label matching. Empirical results are compelling: our 7B model establishes a new state-of-the-art on the Fitzpatrick17k benchmark, achieving a +12.06% gain in Top-1 accuracy and a +28.57% boost in Top-6 accuracy over the massive general-purpose models (e.g., Qwen3VL-235B and GPT-5.2). These findings demonstrate that optimizing geometric capacity and information flow yields superior diagnostic reasoning compared to raw parameter scaling.

