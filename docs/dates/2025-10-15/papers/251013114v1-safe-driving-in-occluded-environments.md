---
layout: default
title: Safe Driving in Occluded Environments
---

# Safe Driving in Occluded Environments
**arXiv**：[2510.13114v1](https://arxiv.org/abs/2510.13114) · [PDF](https://arxiv.org/pdf/2510.13114.pdf)  
**作者**：Zhuoyuan Wang, Tongyao Jia, Pharuj Rajborirug, Neeraj Ramesh, Hiroyuki Okuda, Tatsuya Suzuki, Soummya Kar, Yorie Nakahira  

**一句话要点**：提出概率安全证书以解决遮挡环境中的潜在风险问题

**关键词**：概率安全证书, 遮挡环境, 潜在风险, 模型预测控制, 数据驱动策略, CARLA模拟器

## 3 点简述
- 核心问题：遮挡导致潜在风险，现有模型驱动和数据驱动方法难以处理不可观测的安全关键状态
- 方法要点：应用概率不变性，放宽可观测性要求，提供线性动作约束以控制潜在风险概率
- 实验或效果：在CARLA模拟器中测试，理论分析和实证显示方法确保长期安全且不过度保守

## 摘要（原文）

> Ensuring safe autonomous driving in the presence of occlusions poses a
> significant challenge in its policy design. While existing model-driven control
> techniques based on set invariance can handle visible risks, occlusions create
> latent risks in which safety-critical states are not observable. Data-driven
> techniques also struggle to handle latent risks because direct mappings from
> risk-critical objects in sensor inputs to safe actions cannot be learned
> without visible risk-critical objects. Motivated by these challenges, in this
> paper, we propose a probabilistic safety certificate for latent risk. Our key
> technical enabler is the application of probabilistic invariance: It relaxes
> the strict observability requirements imposed by set-invariance methods that
> demand the knowledge of risk-critical states. The proposed techniques provide
> linear action constraints that confine the latent risk probability within
> tolerance. Such constraints can be integrated into model predictive controllers
> or embedded in data-driven policies to mitigate latent risks. The proposed
> method is tested using the CARLA simulator and compared with a few existing
> techniques. The theoretical and empirical analysis jointly demonstrate that the
> proposed methods assure long-term safety in real-time control in occluded
> environments without being overly conservative and with transparency to exposed
> risks.

