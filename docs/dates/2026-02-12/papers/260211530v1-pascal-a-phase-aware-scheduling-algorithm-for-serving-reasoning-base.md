---
layout: default
title: PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models
---

# PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models
**arXiv**：[2602.11530v1](https://arxiv.org/abs/2602.11530) · [PDF](https://arxiv.org/pdf/2602.11530.pdf)  
**作者**：Eunyeong Cho, Jehyeon Bang, Ranggi Hwang, Minsoo Rhu  

**一句话要点**：提出PASCAL算法以解决推理型大语言模型服务中的阶段感知调度问题

**关键词**：推理型大语言模型, 阶段感知调度, 时间到首令牌优化, 服务质量保证, GPU内存约束

## 3 点简述
- 核心问题：推理型LLM的推理阶段延迟用户可见输出，现有框架未区分阶段导致性能下降
- 方法要点：采用阶段感知调度，优先推理以减少TTFT，并在回答阶段使用受控抢占和令牌步调
- 实验或效果：在DeepSeek-R1-Distill-Qwen-32B基准上，尾部TTFT降低达72%，保持回答阶段SLO达成

## 摘要（原文）

> The emergence of reasoning-based LLMs leveraging Chain-of-Thought (CoT) inference introduces new serving challenges, as their extended reasoning phases delay user-visible output and inflate Time-To-First-Token (TTFT). Existing LLM serving frameworks fail to distinguish between reasoning and answering phases, leading to performance degradation under GPU memory constraints. We present PASCAL, a phase-aware scheduling algorithm that prioritizes reasoning to reduce TTFT while using controlled preemption and token pacing during answering to preserve Quality-of-Experience (QoE). Our hierarchical scheduler combines instance-level placement with intra-instance execution and enables dynamic migration at phase boundaries to balance load and reduce interference. Across benchmarks using DeepSeek-R1-Distill-Qwen-32B, PASCAL reduces tail TTFT by up to 72% while maintaining answering phase SLO attainment, demonstrating the importance of phase-aware scheduling for reasoning-based LLM deployment.

