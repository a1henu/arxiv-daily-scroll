---
layout: default
title: Rectifying LLM Thought from Lens of Optimization
---

# Rectifying LLM Thought from Lens of Optimization
**arXiv**：[2512.01925v1](https://arxiv.org/abs/2512.01925) · [PDF](https://arxiv.org/pdf/2512.01925.pdf)  
**作者**：Junnan Liu, Hongwei Liu, Songyang Zhang, Kai Chen  

**一句话要点**：提出RePro方法，通过优化视角修正大语言模型推理过程，提升性能。

**关键词**：大语言模型, 链式思维推理, 过程级奖励, 强化学习, 优化视角

## 3 点简述
- 核心问题：长链思维推理模型存在过度思考和冗长推理链等次优行为，影响性能。
- 方法要点：将链式思维视为梯度下降过程，定义过程级奖励函数，结合强化学习优化模型。
- 实验或效果：在数学、科学和编码基准测试中，RePro能一致提升推理性能并缓解次优行为。

## 摘要（原文）

> Recent advancements in large language models (LLMs) have been driven by their emergent reasoning capabilities, particularly through long chain-of-thought (CoT) prompting, which enables thorough exploration and deliberation. Despite these advances, long-CoT LLMs often exhibit suboptimal reasoning behaviors, such as overthinking and excessively protracted reasoning chains, which can impair performance. In this paper, we analyze reasoning processes through an optimization lens, framing CoT as a gradient descent procedure where each reasoning step constitutes an update toward problem resolution. Building on this perspective, we introduce RePro (Rectifying Process-level Reward), a novel approach to refine LLM reasoning during post-training. RePro defines a surrogate objective function to assess the optimization process underlying CoT, utilizing a dual scoring mechanism to quantify its intensity and stability. These scores are aggregated into a composite process-level reward, seamlessly integrated into reinforcement learning with verifiable rewards (RLVR) pipelines to optimize LLMs. Extensive experiments across multiple reinforcement learning algorithms and diverse LLMs, evaluated on benchmarks spanning mathematics, science, and coding, demonstrate that RePro consistently enhances reasoning performance and mitigates suboptimal reasoning behaviors.

