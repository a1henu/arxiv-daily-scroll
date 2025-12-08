---
layout: default
title: ProPhy: Progressive Physical Alignment for Dynamic World Simulation
---

# ProPhy: Progressive Physical Alignment for Dynamic World Simulation
**arXiv**：[2512.05564v1](https://arxiv.org/abs/2512.05564) · [PDF](https://arxiv.org/pdf/2512.05564.pdf)  
**作者**：Zijun Wang, Panwen Hu, Jing Wang, Terry Jingchen Zhang, Yuhao Cheng, Long Chen, Yiqiang Yan, Zutao Jiang, Hanhui Li, Xiaodan Liang  

**一句话要点**：提出ProPhy框架以解决视频生成中物理一致性问题，通过渐进物理对齐提升动态世界模拟效果。

**关键词**：视频生成, 物理一致性, 动态世界模拟, 混合物理专家, 渐进对齐, 物理感知条件化

## 3 点简述
- 当前视频生成模型在处理大规模或复杂动态时，因各向同性响应物理提示而缺乏细粒度对齐，导致物理一致性不足。
- ProPhy采用两阶段混合物理专家机制，包括语义专家和细化专家，实现显式物理感知条件化和各向异性生成。
- 在物理感知视频生成基准测试中，ProPhy相比现有方法产生更真实、动态且物理连贯的结果。

## 摘要（原文）

> Recent advances in video generation have shown remarkable potential for constructing world simulators. However, current models still struggle to produce physically consistent results, particularly when handling large-scale or complex dynamics. This limitation arises primarily because existing approaches respond isotropically to physical prompts and neglect the fine-grained alignment between generated content and localized physical cues. To address these challenges, we propose ProPhy, a Progressive Physical Alignment Framework that enables explicit physics-aware conditioning and anisotropic generation. ProPhy employs a two-stage Mixture-of-Physics-Experts (MoPE) mechanism for discriminative physical prior extraction, where Semantic Experts infer semantic-level physical principles from textual descriptions, and Refinement Experts capture token-level physical dynamics. This mechanism allows the model to learn fine-grained, physics-aware video representations that better reflect underlying physical laws. Furthermore, we introduce a physical alignment strategy that transfers the physical reasoning capabilities of vision-language models (VLMs) into the Refinement Experts, facilitating a more accurate representation of dynamic physical phenomena. Extensive experiments on physics-aware video generation benchmarks demonstrate that ProPhy produces more realistic, dynamic, and physically coherent results than existing state-of-the-art methods.

