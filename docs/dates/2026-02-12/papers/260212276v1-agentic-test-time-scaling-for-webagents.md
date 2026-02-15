---
layout: default
title: Agentic Test-Time Scaling for WebAgents
---

# Agentic Test-Time Scaling for WebAgents
**arXiv**：[2602.12276v1](https://arxiv.org/abs/2602.12276) · [PDF](https://arxiv.org/pdf/2602.12276.pdf)  
**作者**：Nicholas Lee, Lutfi Eren Erdogan, Chris Joseph John, Surya Krishnapillai, Michael W. Mahoney, Kurt Keutzer, Amir Gholami  

**一句话要点**：提出CATTS以动态分配计算资源，提升多步网络代理的测试时性能与效率

**关键词**：测试时缩放, 多步代理, 动态计算分配, 不确定性估计, 网络代理, 长视野任务

## 3 点简述
- 核心问题：测试时缩放中，均匀增加计算在长视野任务中效果饱和，小错误会累积
- 方法要点：基于投票分布的不确定性（如熵和边际）动态分配计算，仅在决策有争议时增加资源
- 实验或效果：在WebArena-Lite和GoBrowse上性能提升达9.1%，比均匀缩放节省最多2.3倍令牌

## 摘要（原文）

> Test-time scaling has become a standard way to improve performance and boost reliability of neural network models. However, its behavior on agentic, multi-step tasks remains less well-understood: small per-step errors can compound over long horizons; and we find that naive policies that uniformly increase sampling show diminishing returns. In this work, we present CATTS, a simple technique for dynamically allocating compute for multi-step agents. We first conduct an empirical study of inference-time scaling for web agents. We find that uniformly increasing per-step compute quickly saturates in long-horizon environments. We then investigate stronger aggregation strategies, including an LLM-based Arbiter that can outperform naive voting, but that can overrule high-consensus decisions. We show that uncertainty statistics derived from the agent's own vote distribution (entropy and top-1/top-2 margin) correlate with downstream success and provide a practical signal for dynamic compute allocation. Based on these findings, we introduce Confidence-Aware Test-Time Scaling (CATTS), which uses vote-derived uncertainty to allocate compute only when decisions are genuinely contentious. CATTS improves performance on WebArena-Lite and GoBrowse by up to 9.1% over React while using up to 2.3x fewer tokens than uniform scaling, providing both efficiency gains and an interpretable decision rule.

