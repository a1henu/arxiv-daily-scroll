---
layout: default
title: Exploring the Temporal Consistency for Point-Level Weakly-Supervised Temporal Action Localization
---

# Exploring the Temporal Consistency for Point-Level Weakly-Supervised Temporal Action Localization
**arXiv**：[2602.05718v1](https://arxiv.org/abs/2602.05718) · [PDF](https://arxiv.org/pdf/2602.05718.pdf)  
**作者**：Yunchuan Ma, Laiyun Qing, Guorong Li, Yuqing Liu, Yuankai Qi, Qingming Huang  

**一句话要点**：提出多任务学习框架，通过自监督时序理解任务增强点监督时序动作定位的时序一致性建模。

**关键词**：点监督时序动作定位, 自监督学习, 时序一致性, 多任务学习, 长视频理解

## 3 点简述
- 核心问题：点监督时序动作定位中，现有方法缺乏对动作帧间时序关系的显式建模，影响动作完整定位。
- 方法要点：设计三个自监督时序理解任务（动作完成、动作顺序理解、动作规律理解），以提升模型对动作时序一致性的理解能力。
- 实验或效果：在四个基准数据集上验证了方法的有效性，优于多个先进方法。

## 摘要（原文）

> Point-supervised Temporal Action Localization (PTAL) adopts a lightly frame-annotated paradigm (\textit{i.e.}, labeling only a single frame per action instance) to train a model to effectively locate action instances within untrimmed videos. Most existing approaches design the task head of models with only a point-supervised snippet-level classification, without explicit modeling of understanding temporal relationships among frames of an action. However, understanding the temporal relationships of frames is crucial because it can help a model understand how an action is defined and therefore benefits localizing the full frames of an action. To this end, in this paper, we design a multi-task learning framework that fully utilizes point supervision to boost the model's temporal understanding capability for action localization. Specifically, we design three self-supervised temporal understanding tasks: (i) Action Completion, (ii) Action Order Understanding, and (iii) Action Regularity Understanding. These tasks help a model understand the temporal consistency of actions across videos. To the best of our knowledge, this is the first attempt to explicitly explore temporal consistency for point supervision action localization. Extensive experimental results on four benchmark datasets demonstrate the effectiveness of the proposed method compared to several state-of-the-art approaches.

