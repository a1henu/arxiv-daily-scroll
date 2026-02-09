---
layout: default
title: Agentic Uncertainty Reveals Agentic Overconfidence
---

# Agentic Uncertainty Reveals Agentic Overconfidence
**arXiv**：[2602.06948v1](https://arxiv.org/abs/2602.06948) · [PDF](https://arxiv.org/pdf/2602.06948.pdf)  
**作者**：Jean Kaddour, Srijan Patel, Gbètondji Dovonon, Leo Richter, Pasquale Minervini, Matt J. Kusner  

**一句话要点**：提出代理不确定性评估方法，揭示AI代理在任务执行中的过度自信现象。

**关键词**：代理不确定性, 过度自信, 概率估计, 对抗性提示, 任务执行评估

## 3 点简述
- 研究AI代理能否预测任务成功率，通过执行前、中、后概率估计评估代理不确定性。
- 发现代理过度自信，例如成功率仅22%时预测77%，且执行前评估有时优于执行后。
- 采用对抗性提示将评估重构为错误查找，实现最佳校准效果。

## 摘要（原文）

> Can AI agents predict whether they will succeed at a task? We study agentic uncertainty by eliciting success probability estimates before, during, and after task execution. All results exhibit agentic overconfidence: some agents that succeed only 22% of the time predict 77% success. Counterintuitively, pre-execution assessment with strictly less information tends to yield better discrimination than standard post-execution review, though differences are not always significant. Adversarial prompting reframing assessment as bug-finding achieves the best calibration.

