---
layout: default
title: Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models
---

# Dynamic Thinking-Token Selection for Efficient Reasoning in Large Reasoning Models
**arXiv**：[2601.18383v1](https://arxiv.org/abs/2601.18383) · [PDF](https://arxiv.org/pdf/2601.18383.pdf)  
**作者**：Zhenyuan Guo, Tong Chen, Wenlong Meng, Chen Gong, Xin Yu, Chengkun Wei, Wenzhi Chen  

**一句话要点**：提出动态思维令牌选择方法以优化大型推理模型的推理效率

**关键词**：大型推理模型, 注意力机制, KV缓存优化, 推理效率, 动态令牌选择

## 3 点简述
- 大型推理模型生成推理轨迹导致内存和计算开销大
- 基于注意力图分析发现仅决策关键令牌对最终答案有显著影响
- DynTS方法在推理时仅保留关键令牌的KV缓存以提升效率

## 摘要（原文）

> Large Reasoning Models (LRMs) excel at solving complex problems by explicitly generating a reasoning trace before deriving the final answer. However, these extended generations incur substantial memory footprint and computational overhead, bottlenecking LRMs' efficiency. This work uses attention maps to analyze the influence of reasoning traces and uncover an interesting phenomenon: only some decision-critical tokens in a reasoning trace steer the model toward the final answer, while the remaining tokens contribute negligibly. Building on this observation, we propose Dynamic Thinking-Token Selection (DynTS). This method identifies decision-critical tokens and retains only their associated Key-Value (KV) cache states during inference, evicting the remaining redundant entries to optimize efficiency.

