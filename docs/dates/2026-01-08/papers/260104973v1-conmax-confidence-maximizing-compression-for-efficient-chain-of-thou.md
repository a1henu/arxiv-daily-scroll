---
layout: default
title: ConMax: Confidence-Maximizing Compression for Efficient Chain-of-Thought Reasoning
---

# ConMax: Confidence-Maximizing Compression for Efficient Chain-of-Thought Reasoning
**arXiv**：[2601.04973v1](https://arxiv.org/abs/2601.04973) · [PDF](https://arxiv.org/pdf/2601.04973.pdf)  
**作者**：Minda Hu, Zexuan Qiu, Zenan Xu, Kun Li, Bo Zhou, Irwin King  

**一句话要点**：提出ConMax强化学习框架，通过置信度最大化压缩推理轨迹以提升大型推理模型效率

**关键词**：推理轨迹压缩, 强化学习优化, 置信度最大化, 大型推理模型, 链式思维推理

## 3 点简述
- 大型推理模型生成冗余推理路径导致计算成本过高，现有压缩技术会损害逻辑连贯性或采样成本过高
- ConMax将压缩建模为奖励驱动的优化问题，通过最大化答案置信度和思考置信度来剪枝冗余
- 在五个推理数据集上实验显示，推理长度减少43%而准确率仅下降0.7%

## 摘要（原文）

> Recent breakthroughs in Large Reasoning Models (LRMs) have demonstrated that extensive Chain-of-Thought (CoT) generation is critical for enabling intricate cognitive behaviors, such as self-verification and backtracking, to solve complex tasks. However, this capability often leads to ``overthinking'', where models generate redundant reasoning paths that inflate computational costs without improving accuracy. While Supervised Fine-Tuning (SFT) on reasoning traces is a standard paradigm for the 'cold start' phase, applying existing compression techniques to these traces often compromises logical coherence or incurs prohibitive sampling costs. In this paper, we introduce ConMax (Confidence-Maximizing Compression), a novel reinforcement learning framework designed to automatically compress reasoning traces while preserving essential reasoning patterns. ConMax formulates compression as a reward-driven optimization problem, training a policy to prune redundancy by maximizing a weighted combination of answer confidence for predictive fidelity and thinking confidence for reasoning validity through a frozen auxiliary LRM. Extensive experiments across five reasoning datasets demonstrate that ConMax achieves a superior efficiency-performance trade-off. Specifically, it reduces inference length by 43% over strong baselines at the cost of a mere 0.7% dip in accuracy, proving its effectiveness in generating high-quality, efficient training data for LRMs.

