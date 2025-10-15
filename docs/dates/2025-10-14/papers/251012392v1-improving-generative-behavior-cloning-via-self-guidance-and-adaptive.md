---
layout: default
title: Improving Generative Behavior Cloning via Self-Guidance and Adaptive Chunking
---

# Improving Generative Behavior Cloning via Self-Guidance and Adaptive Chunking
**arXiv**：[2510.12392v1](https://arxiv.org/abs/2510.12392) · [PDF](https://arxiv.org/pdf/2510.12392.pdf)  
**作者**：Junhyuk So, Chiwoong Lee, Shinyoung Lee, Jungseul Ok, Eunhyeok Park  

**一句话要点**：提出自引导与自适应分块以提升生成行为克隆在机器人学习中的一致性与反应性

**关键词**：生成行为克隆, 扩散策略, 自引导, 自适应分块, 机器人学习, 多任务学习

## 3 点简述
- 核心问题：扩散策略在开环控制中因随机性导致动作错误和延迟响应，影响任务性能。
- 方法要点：引入自引导利用过去观察提升动作保真度，自适应分块根据需求选择性更新动作序列。
- 实验或效果：在模拟和真实机器人操作任务中显著提升性能，代码已开源。

## 摘要（原文）

> Generative Behavior Cloning (GBC) is a simple yet effective framework for
> robot learning, particularly in multi-task settings. Recent GBC methods often
> employ diffusion policies with open-loop (OL) control, where actions are
> generated via a diffusion process and executed in multi-step chunks without
> replanning. While this approach has demonstrated strong success rates and
> generalization, its inherent stochasticity can result in erroneous action
> sampling, occasionally leading to unexpected task failures. Moreover, OL
> control suffers from delayed responses, which can degrade performance in noisy
> or dynamic environments. To address these limitations, we propose two novel
> techniques to enhance the consistency and reactivity of diffusion policies: (1)
> self-guidance, which improves action fidelity by leveraging past observations
> and implicitly promoting future-aware behavior; and (2) adaptive chunking,
> which selectively updates action sequences when the benefits of reactivity
> outweigh the need for temporal consistency. Extensive experiments show that our
> approach substantially improves GBC performance across a wide range of
> simulated and real-world robotic manipulation tasks. Our code is available at
> https://github.com/junhyukso/SGAC

