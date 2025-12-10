---
layout: default
title: HybridToken-VLM: Hybrid Token Compression for Vision-Language Models
---

# HybridToken-VLM: Hybrid Token Compression for Vision-Language Models
**arXiv**：[2512.08240v1](https://arxiv.org/abs/2512.08240) · [PDF](https://arxiv.org/pdf/2512.08240.pdf)  
**作者**：Jusheng Zhang, Xiaoyang Guo, Kaitong Cai, Qinhan Lv, Yijia Fan, Wenhao Chai, Jian Wang, Keze Wang  

**一句话要点**：提出混合令牌压缩框架HTC-VLM，通过双通道解耦语义与外观，解决视觉语言模型的计算效率与表示保真度困境。

**关键词**：视觉语言模型, 令牌压缩, 混合表示, 计算效率, 多模态推理, 解耦注意力

## 3 点简述
- 视觉语言模型中大量视觉补丁令牌导致二次计算成本，传统连续压缩与离散量化方法各有缺陷。
- 采用双通道混合设计：连续路径保留细粒度细节，离散路径通过MGVQ量化生成符号锚点，融合后压缩为单一令牌。
- 在七个基准测试中平均性能保持87.2%，以580:1压缩比优于连续基线，注意力分析验证语义引导有效性。

## 摘要（原文）

> Vision-language models (VLMs) have transformed multimodal reasoning, but feeding hundreds of visual patch tokens into LLMs incurs quadratic computational costs, straining memory and context windows. Traditional approaches face a trade-off: continuous compression dilutes high-level semantics such as object identities, while discrete quantization loses fine-grained details such as textures. We introduce HTC-VLM, a hybrid framework that disentangles semantics and appearance through dual channels, i.e., a continuous pathway for fine-grained details via ViT patches and a discrete pathway for symbolic anchors using MGVQ quantization projected to four tokens. These are fused into a 580-token hybrid sequence and compressed into a single voco token via a disentanglement attention mask and bottleneck, ensuring efficient and grounded representations. HTC-VLM achieves an average performance retention of 87.2 percent across seven benchmarks (GQA, VQAv2, MMBench, MME, POPE, SEED-Bench, ScienceQA-Image), outperforming the leading continuous baseline at 81.0 percent with a 580-to-1 compression ratio. Attention analyses show that the compressed token prioritizes the discrete anchor, validating its semantic guidance. Our work demonstrates that a minimalist hybrid design can resolve the efficiency-fidelity dilemma and advance scalable VLMs.

