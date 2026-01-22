---
layout: default
title: V-CAGE: Context-Aware Generation and Verification for Scalable Long-Horizon Embodied Tasks
---

# V-CAGE: Context-Aware Generation and Verification for Scalable Long-Horizon Embodied Tasks
**arXiv**：[2601.15164v1](https://arxiv.org/abs/2601.15164) · [PDF](https://arxiv.org/pdf/2601.15164.pdf)  
**作者**：Yaru Liu, Ao-bo Wang, Nanyang Ye  

**一句话要点**：提出V-CAGE框架以解决长时程具身任务中场景生成与语义对齐的挑战

**关键词**：具身智能, 长时程任务, 场景生成, 语义验证, 分层规划, 数据集构建

## 3 点简述
- 核心问题：合成数据生成的场景常物理不可行，语言程序执行可能未满足任务语义，高层指令需接地为可执行动作序列。
- 方法要点：采用上下文感知实例化机制确保几何一致性，分层指令分解模块将目标分解为动作基元，基于VLM的验证循环过滤语义错误。
- 实验或效果：V-CAGE生成的数据集物理和语义保真度高，显著提升下游策略的成功率和泛化能力。

## 摘要（原文）

> Learning long-horizon embodied behaviors from synthetic data remains challenging because generated scenes are often physically implausible, language-driven programs frequently "succeed" without satisfying task semantics, and high-level instructions require grounding into executable action sequences. To address these limitations, we introduce V-CAGE, a closed-loop framework for generating robust, semantically aligned manipulation datasets at scale. First, we propose a context-aware instantiation mechanism that enforces geometric consistency during scene synthesis. By dynamically maintaining a map of prohibited spatial areas as objects are placed, our system prevents interpenetration and ensures reachable, conflict-free configurations in cluttered environments. Second, to bridge the gap between abstract intent and low-level control, we employ a hierarchical instruction decomposition module. This decomposes high-level goals (e.g., "get ready for work") into compositional action primitives, facilitating coherent long-horizon planning. Crucially, we enforce semantic correctness through a VLM-based verification loop. Acting as a visual critic, the VLM performs rigorous rejection sampling after each subtask, filtering out "silent failures" where code executes but fails to achieve the visual goal. Experiments demonstrate that V-CAGE yields datasets with superior physical and semantic fidelity, significantly boosting the success rate and generalization of downstream policies compared to non-verified baselines.

