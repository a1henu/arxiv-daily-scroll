---
layout: default
title: Spatio-Temporal Token Pruning for Efficient High-Resolution GUI Agents
---

# Spatio-Temporal Token Pruning for Efficient High-Resolution GUI Agents
**arXiv**：[2602.23235v1](https://arxiv.org/abs/2602.23235) · [PDF](https://arxiv.org/pdf/2602.23235.pdf)  
**作者**：Zhou Xu, Bowen Zhou, Qi Wang, Shuwen Feng, Jingyu Xiao  

**一句话要点**：提出GUIPruner框架以解决高分辨率GUI代理中的时空冗余问题

**关键词**：GUI代理, 时空剪枝, 高分辨率视觉, 效率优化, 无训练框架

## 3 点简述
- 核心问题：高分辨率截图和历史轨迹存在时空冗余，导致效率瓶颈和空间幻觉
- 方法要点：结合时间自适应分辨率和分层结构感知剪枝，无训练地压缩视觉输入
- 实验或效果：在Qwen2-VL-2B上实现3.4倍FLOPs减少和3.3倍加速，性能保留超94%

## 摘要（原文）

> Pure-vision GUI agents provide universal interaction capabilities but suffer from severe efficiency bottlenecks due to the massive spatiotemporal redundancy inherent in high-resolution screenshots and historical trajectories. We identify two critical misalignments in existing compression paradigms: the temporal mismatch, where uniform history encoding diverges from the agent's "fading memory" attention pattern, and the spatial topology conflict, where unstructured pruning compromises the grid integrity required for precise coordinate grounding, inducing spatial hallucinations. To address these challenges, we introduce GUIPruner, a training-free framework tailored for high-resolution GUI navigation. It synergizes Temporal-Adaptive Resolution (TAR), which eliminates historical redundancy via decay-based resizing, and Stratified Structure-aware Pruning (SSP), which prioritizes interactive foregrounds and semantic anchors while safeguarding global layout. Extensive evaluations across diverse benchmarks demonstrate that GUIPruner consistently achieves state-of-the-art performance, effectively preventing the collapse observed in large-scale models under high compression. Notably, on Qwen2-VL-2B, our method delivers a 3.4x reduction in FLOPs and a 3.3x speedup in vision encoding latency while retaining over 94% of the original performance, enabling real-time, high-precision navigation with minimal resource consumption.

