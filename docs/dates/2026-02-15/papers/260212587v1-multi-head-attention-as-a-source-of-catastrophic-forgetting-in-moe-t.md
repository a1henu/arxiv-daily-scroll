---
layout: default
title: Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers
---

# Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers
**arXiv**：[2602.12587v1](https://arxiv.org/abs/2602.12587) · [PDF](https://arxiv.org/pdf/2602.12587.pdf)  
**作者**：Anrui Chen, Ruijun Huang, Xin Zhang, Fang Dong, Hengjie Cao, Zhendong Huang, Yifeng Yang, Mengyi Chen, Jixian Zhou, Mingzhi Dong, Yujiang Wang, Jinlong Hou, Qin Lv, Robert P. Dick, Yuan Cheng, Tun Lu, Fan Yang, Li Shang  

**一句话要点**：提出MH-MoE以解决MoE Transformer中多头注意力导致的灾难性遗忘问题

**关键词**：MoE Transformer, 灾难性遗忘, 多头注意力, 路由机制, 持续学习

## 3 点简述
- 核心问题：MoE Transformer中多头注意力预路由瓶颈导致特征组合碰撞，引发灾难性遗忘
- 方法要点：MH-MoE通过头级路由增加路由粒度，减少组合碰撞
- 实验或效果：在TRACE数据集上，MH-MoE显著降低遗忘，BWT从11.2%降至4.5%

## 摘要（原文）

> Mixture-of-Experts (MoE) architectures are often considered a natural fit for continual learning because sparse routing should localize updates and reduce interference, yet MoE Transformers still forget substantially even with sparse, well-balanced expert utilization. We attribute this gap to a pre-routing bottleneck: multi-head attention concatenates head-specific signals into a single post-attention router input, forcing routing to act on co-occurring feature compositions rather than separable head channels. We show that this router input simultaneously encodes multiple separately decodable semantic and structural factors with uneven head support, and that different feature compositions induce weakly aligned parameter-gradient directions; as a result, routing maps many distinct compositions to the same route. We quantify this collision effect via a route-wise effective composition number $N_{eff}$ and find that higher $N_{eff}$ is associated with larger old-task loss increases after continual training. Motivated by these findings, we propose MH-MoE, which performs head-wise routing over sub-representations to increase routing granularity and reduce composition collisions. On TRACE with Qwen3-0.6B/8B, MH-MoE effectively mitigates forgetting, reducing BWT on Qwen3-0.6B from 11.2% (LoRAMoE) to 4.5%.

