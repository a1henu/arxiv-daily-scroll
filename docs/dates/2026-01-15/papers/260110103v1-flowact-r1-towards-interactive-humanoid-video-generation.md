---
layout: default
title: FlowAct-R1: Towards Interactive Humanoid Video Generation
---

# FlowAct-R1: Towards Interactive Humanoid Video Generation
**arXiv**：[2601.10103v1](https://arxiv.org/abs/2601.10103) · [PDF](https://arxiv.org/pdf/2601.10103.pdf)  
**作者**：Lizhen Wang, Yongming Zhu, Zhipeng Ge, Youwei Zheng, Longhao Zhang, Tianshu Hu, Shiyang Qin, Mingshuang Luo, Jiaxu Zhang, Xin Chen, Yulong Wang, Zerong Zheng, Jianwen Jiang, Chao Liang, Weifeng Chen, Xing Wang, Yuan Zhang, Mingyuan Gao  

**一句话要点**：提出FlowAct-R1框架以解决实时交互人形视频生成中高保真与低延迟的权衡问题

**关键词**：实时视频生成, 人形交互, 分块扩散, 时间一致性, 蒸馏优化, 全身体控制

## 3 点简述
- 核心问题：现有方法在视频合成中难以平衡高保真度与实时交互需求
- 方法要点：基于MMDiT架构，采用分块扩散强制策略确保长期时间一致性
- 实验或效果：在480p分辨率下实现25fps稳定生成，首帧延迟约1.5秒，展现高行为生动性

## 摘要（原文）

> Interactive humanoid video generation aims to synthesize lifelike visual agents that can engage with humans through continuous and responsive video. Despite recent advances in video synthesis, existing methods often grapple with the trade-off between high-fidelity synthesis and real-time interaction requirements. In this paper, we propose FlowAct-R1, a framework specifically designed for real-time interactive humanoid video generation. Built upon a MMDiT architecture, FlowAct-R1 enables the streaming synthesis of video with arbitrary durations while maintaining low-latency responsiveness. We introduce a chunkwise diffusion forcing strategy, complemented by a novel self-forcing variant, to alleviate error accumulation and ensure long-term temporal consistency during continuous interaction. By leveraging efficient distillation and system-level optimizations, our framework achieves a stable 25fps at 480p resolution with a time-to-first-frame (TTFF) of only around 1.5 seconds. The proposed method provides holistic and fine-grained full-body control, enabling the agent to transition naturally between diverse behavioral states in interactive scenarios. Experimental results demonstrate that FlowAct-R1 achieves exceptional behavioral vividness and perceptual realism, while maintaining robust generalization across diverse character styles.

