---
layout: default
title: Learning with Multiple Correct Answers -- A Trichotomy of Regret Bounds under Different Feedback Models
---

# Learning with Multiple Correct Answers -- A Trichotomy of Regret Bounds under Different Feedback Models
**arXiv**：[2602.09402v1](https://arxiv.org/abs/2602.09402) · [PDF](https://arxiv.org/pdf/2602.09402.pdf)  
**作者**：Alireza F. Pour, Farnam Mansouri, Shai Ben-David  

**一句话要点**：提出多正确答案在线学习框架，基于三种反馈模型分析遗憾界三分法。

**关键词**：在线学习, 多正确答案, 遗憾界, 组合维度, 反馈模型, 语言生成

## 3 点简述
- 研究多正确答案在线学习问题，每个实例有多个有效标签，学习者需输出有效标签。
- 在可实现设置中，使用组合维度刻画最优错误界；在不可知设置中，建立三种反馈模型的遗憾界三分法。
- 结果暗示批量设置的样本复杂度界依赖于相应组合维度，适用于语言生成等任务。

## 摘要（原文）

> We study an online learning problem with multiple correct answers, where each instance admits a set of valid labels, and in each round the learner must output a valid label for the queried example. This setting is motivated by language generation tasks, in which a prompt may admit many acceptable completions, but not every completion is acceptable. We study this problem under three feedback models. For each model, we characterize the optimal mistake bound in the realizable setting using an appropriate combinatorial dimension. We then establish a trichotomy of regret bounds across the three models in the agnostic setting. Our results also imply sample complexity bounds for the batch setup that depend on the respective combinatorial dimensions.

