---
layout: default
title: Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors
---

# Robust Tool Use via Fission-GRPO: Learning to Recover from Execution Errors
**arXiv**：[2601.15625v1](https://arxiv.org/abs/2601.15625) · [PDF](https://arxiv.org/pdf/2601.15625.pdf)  
**作者**：Zhiwei Zhang, Fei Zhao, Rui Wang, Zezhong Wang, Bin Liang, Jiakang Wang, Yao Hu, Shaosheng Cao, Kam-Fai Wong  

**一句话要点**：提出Fission-GRPO框架，通过将执行错误转化为纠正监督，提升大语言模型在工具调用中的错误恢复能力。

**关键词**：工具调用, 错误恢复, 强化学习, 大语言模型, 多轮执行

## 3 点简述
- 核心问题：大语言模型在多轮工具调用中，面对执行错误时易退化，无法有效自我纠正，阻碍实际部署。
- 方法要点：在强化学习训练循环中，利用错误模拟器诊断失败轨迹，生成新训练实例，使模型从自身探索错误中学习恢复。
- 实验或效果：在BFCL v4 Multi-Turn基准上，Fission-GRPO显著提升Qwen3-8B的错误恢复率和整体准确率，优于现有方法。

## 摘要（原文）

> Large language models (LLMs) can call tools effectively, yet they remain brittle in multi-turn execution: following a tool call error, smaller models often degenerate into repetitive invalid re-invocations, failing to interpret error feedback and self-correct. This brittleness hinders reliable real-world deployment, where the execution errors are inherently inevitable during tool interaction procedures. We identify a key limitation of current approaches: standard reinforcement learning (RL) treats errors as sparse negative rewards, providing no guidance on how to recover, while pre-collected synthetic error-correction datasets suffer from distribution mismatch with the model's on-policy error modes. To bridge this gap, we propose Fission-GRPO, a framework that converts execution errors into corrective supervision within the RL training loop. Our core mechanism fissions each failed trajectory into a new training instance by augmenting it with diagnostic feedback from a finetuned Error Simulator, then resampling recovery rollouts on-policy. This enables the model to learn from the precise errors it makes during exploration, rather than from static, pre-collected error cases. On the BFCL v4 Multi-Turn, Fission-GRPO improves the error recovery rate of Qwen3-8B by 5.7% absolute, crucially, yielding a 4% overall accuracy gain (42.75% to 46.75%) over GRPO and outperforming specialized tool-use agents.

