---
layout: default
title: Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects
---

# Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects
**arXiv**：[2510.09269v1](https://arxiv.org/abs/2510.09269) · [PDF](https://arxiv.org/pdf/2510.09269.pdf)  
**作者**：Zirun Zhou, Zhengyang Xiao, Haochuan Xu, Jing Sun, Di Wang, Jingfeng Zhang  

**一句话要点**：提出目标导向后门攻击，通过物理对象操纵视觉-语言-动作模型

**关键词**：后门攻击, 视觉-语言-动作模型, 物理触发器, 目标导向动作, 安全评估, 数据集污染

## 3 点简述
- 视觉-语言-动作模型依赖未筛选数据集，存在安全风险，现有攻击多为白盒且导致任务失败
- 引入物理对象作为触发器，在触发时执行预设目标动作，不影响正常输入性能
- 实验显示攻击成功率97%，动作轨迹和触发器颜色显著影响性能，代码和数据集已公开

## 摘要（原文）

> Recent advances in vision-language-action (VLA) models have greatly improved
> embodied AI, enabling robots to follow natural language instructions and
> perform diverse tasks. However, their reliance on uncurated training datasets
> raises serious security concerns. Existing backdoor attacks on VLAs mostly
> assume white-box access and result in task failures instead of enforcing
> specific actions. In this work, we reveal a more practical threat: attackers
> can manipulate VLAs by simply injecting physical objects as triggers into the
> training dataset. We propose goal-oriented backdoor attacks (GoBA), where the
> VLA behaves normally in the absence of physical triggers but executes
> predefined and goal-oriented actions in the presence of physical triggers.
> Specifically, based on a popular VLA benchmark LIBERO, we introduce BadLIBERO
> that incorporates diverse physical triggers and goal-oriented backdoor actions.
> In addition, we propose a three-level evaluation that categorizes the victim
> VLA's actions under GoBA into three states: nothing to do, try to do, and
> success to do. Experiments show that GoBA enables the victim VLA to
> successfully achieve the backdoor goal in 97 percentage of inputs when the
> physical trigger is present, while causing zero performance degradation on
> clean inputs. Finally, by investigating factors related to GoBA, we find that
> the action trajectory and trigger color significantly influence attack
> performance, while trigger size has surprisingly little effect. The code and
> BadLIBERO dataset are accessible via the project page at
> https://goba-attack.github.io/.

