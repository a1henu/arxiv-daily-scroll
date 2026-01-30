---
layout: default
title: Do Not Waste Your Rollouts: Recycling Search Experience for Efficient Test-Time Scaling
---

# Do Not Waste Your Rollouts: Recycling Search Experience for Efficient Test-Time Scaling
**arXiv**：[2601.21684v1](https://arxiv.org/abs/2601.21684) · [PDF](https://arxiv.org/pdf/2601.21684.pdf)  
**作者**：Xinglin Wang, Jiayi Shi, Shaoxiong Feng, Peiwen Yuan, Yiwei Li, Yueqi Zhang, Chuyi Tan, Ji Zhang, Boyuan Pan, Yao Hu, Kan Li  

**一句话要点**：提出RSE策略以解决测试时扩展中搜索经验浪费问题，通过回收经验提升推理效率。

**关键词**：测试时扩展, 经验回收, 推理效率, 大语言模型, 搜索策略, 计算优化

## 3 点简述
- 核心问题：现有测试时扩展策略丢弃搜索中间经验，导致计算冗余和效率低下。
- 方法要点：RSE通过经验库回收正负经验，实现自引导的累积搜索过程，无需额外训练。
- 实验或效果：在多个基准测试中，RSE以可比计算成本超越基线，达到最优扩展效率。

## 摘要（原文）

> Test-Time Scaling enhances the reasoning capabilities of Large Language Models by allocating additional inference compute to broaden the exploration of the solution space. However, existing search strategies typically treat rollouts as disposable samples, where valuable intermediate insights are effectively discarded after each trial. This systemic memorylessness leads to massive computational redundancy, as models repeatedly re-derive discovered conclusions and revisit known dead ends across extensive attempts. To bridge this gap, we propose \textbf{Recycling Search Experience (RSE)}, a self-guided, training-free strategy that turns test-time search from a series of isolated trials into a cumulative process. By actively distilling raw trajectories into a shared experience bank, RSE enables positive recycling of intermediate conclusions to shortcut redundant derivations and negative recycling of failure patterns to prune encountered dead ends. Theoretically, we provide an analysis that formalizes the efficiency gains of RSE, validating its advantage over independent sampling in solving complex reasoning tasks. Empirically, extensive experiments on HMMT24, HMMT25, IMO-Bench, and HLE show that RSE consistently outperforms strong baselines with comparable computational cost, achieving state-of-the-art scaling efficiency.

