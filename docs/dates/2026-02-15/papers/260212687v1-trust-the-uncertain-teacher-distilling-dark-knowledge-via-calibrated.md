---
layout: default
title: Trust the uncertain teacher: distilling dark knowledge via calibrated uncertainty
---

# Trust the uncertain teacher: distilling dark knowledge via calibrated uncertainty
**arXiv**：[2602.12687v1](https://arxiv.org/abs/2602.12687) · [PDF](https://arxiv.org/pdf/2602.12687.pdf)  
**作者**：Jeonghyun Kim, SooKyung Kim, Richeng Xuan, Hyunsoo Cho  

**一句话要点**：提出校准不确定性蒸馏以解决教师模型过自信导致暗知识传递失效的问题

**关键词**：知识蒸馏, 不确定性校准, 暗知识传递, 分布偏移鲁棒性, 高基数分类任务

## 3 点简述
- 核心问题：传统交叉熵训练的教师模型预测分布尖锐过自信，削弱暗知识传递，影响学生模型在复杂任务和分布偏移下的性能
- 方法要点：通过校准不确定性蒸馏框架，调整教师预测分布，平衡准确性与校准性，使学生从自信信号和结构化不确定性中学习
- 实验或效果：在多样化基准测试中，学生模型准确性提升，校准性增强，在分布偏移和模糊输入下更可靠

## 摘要（原文）

> The core of knowledge distillation lies in transferring the teacher's rich 'dark knowledge'-subtle probabilistic patterns that reveal how classes are related and the distribution of uncertainties. While this idea is well established, teachers trained with conventional cross-entropy often fail to preserve such signals. Their distributions collapse into sharp, overconfident peaks that appear decisive but are in fact brittle, offering little beyond the hard label or subtly hindering representation-level transfer. This overconfidence is especially problematic in high-cardinality tasks, where the nuances among many plausible classes matter most for guiding a compact student. Moreover, such brittle targets reduce robustness under distribution shift, leaving students vulnerable to miscalibration in real-world conditions. To address this limitation, we revisit distillation from a distributional perspective and propose Calibrated Uncertainty Distillation (CUD), a framework designed to make dark knowledge more faithfully accessible. Instead of uncritically adopting the teacher's overconfidence, CUD encourages teachers to reveal uncertainty where it is informative and guides students to learn from targets that are calibrated rather than sharpened certainty. By directly shaping the teacher's predictive distribution before transfer, our approach balances accuracy and calibration, allowing students to benefit from both confident signals on easy cases and structured uncertainty on hard ones. Across diverse benchmarks, CUD yields students that are not only more accurate, but also more calibrated under shift and more reliable on ambiguous, long-tail inputs.

