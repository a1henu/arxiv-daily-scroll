---
layout: default
title: More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization
---

# More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization
**arXiv**：[2512.24545v1](https://arxiv.org/abs/2512.24545) · [PDF](https://arxiv.org/pdf/2512.24545.pdf)  
**作者**：Yuma Ichikawa, Yoshihiko Fujisawa, Yudai Fujimoto, Akira Sakai, Katsuki Fujisawa  

**一句话要点**：提出多包络双二进制分解以解决极端量化中性能饱和问题

**关键词**：极端量化, 双二进制分解, 大语言模型, 低比特推理, 包络优化, 性能提升

## 3 点简述
- 双二进制分解在极端低比特量化中因缩放参数限制导致性能饱和
- MDBF保留1比特符号基，引入秩-l包络提升幅度表达能力
- 在LLaMA和Qwen模型上提升困惑度和零样本准确率，保持部署友好性

## 摘要（原文）

> For extreme low-bit quantization of large language models (LLMs), Double Binary Factorization (DBF) is attractive as it enables efficient inference without sacrificing accuracy. However, the scaling parameters of DBF are too restrictive; after factoring out signs, all rank components share the same magnitude profile, resulting in performance saturation. We propose Multi-envelope DBF (MDBF), which retains a shared pair of 1-bit sign bases but replaces the single envelope with a rank-$l$ envelope. By sharing sign matrices among envelope components, MDBF effectively maintains a binary carrier and utilizes the limited memory budget for magnitude expressiveness. We also introduce a closed-form initialization and an alternating refinement method to optimize MDBF. Across the LLaMA and Qwen families, MDBF enhances perplexity and zero-shot accuracy over previous binary formats at matched bits per weight while preserving the same deployment-friendly inference primitive.

