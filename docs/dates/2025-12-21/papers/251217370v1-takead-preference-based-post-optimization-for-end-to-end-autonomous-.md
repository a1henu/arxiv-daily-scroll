---
layout: default
title: TakeAD: Preference-based Post-optimization for End-to-end Autonomous Driving with Expert Takeover Data
---

# TakeAD: Preference-based Post-optimization for End-to-end Autonomous Driving with Expert Takeover Data
**arXiv**：[2512.17370v1](https://arxiv.org/abs/2512.17370) · [PDF](https://arxiv.org/pdf/2512.17370.pdf)  
**作者**：Deqing Liu, Yinfeng Gao, Deheng Qian, Qichao Zhang, Xiaoqing Ye, Junyu Han, Yupeng Zheng, Xueyi Liu, Zhongpu Xia, Dawei Ding, Yifeng Pan, Dongbin Zhao  

**一句话要点**：提出TakeAD框架，利用专家接管数据优化端到端自动驾驶策略以缓解开环-闭环差距

**关键词**：端到端自动驾驶, 专家接管数据, 偏好优化, 开环-闭环差距, 数据集聚合, 模仿学习

## 3 点简述
- 核心问题：端到端自动驾驶中开环训练与闭环部署的错配导致接管和脱钩，需利用脱钩数据扩展策略能力
- 方法要点：结合迭代数据集聚合模仿专家干预，再通过直接偏好优化对齐专家偏好，分阶段优化策略
- 实验或效果：在Bench2Drive基准上验证优于纯模仿学习方法，消融实验确认各组件贡献

## 摘要（原文）

> Existing end-to-end autonomous driving methods typically rely on imitation learning (IL) but face a key challenge: the misalignment between open-loop training and closed-loop deployment. This misalignment often triggers driver-initiated takeovers and system disengagements during closed-loop execution. How to leverage those expert takeover data from disengagement scenarios and effectively expand the IL policy's capability presents a valuable yet unexplored challenge. In this paper, we propose TakeAD, a novel preference-based post-optimization framework that fine-tunes the pre-trained IL policy with this disengagement data to enhance the closed-loop driving performance. First, we design an efficient expert takeover data collection pipeline inspired by human takeover mechanisms in real-world autonomous driving systems. Then, this post optimization framework integrates iterative Dataset Aggregation (DAgger) for imitation learning with Direct Preference Optimization (DPO) for preference alignment. The DAgger stage equips the policy with fundamental capabilities to handle disengagement states through direct imitation of expert interventions. Subsequently, the DPO stage refines the policy's behavior to better align with expert preferences in disengagement scenarios. Through multiple iterations, the policy progressively learns recovery strategies for disengagement states, thereby mitigating the open-loop gap. Experiments on the closed-loop Bench2Drive benchmark demonstrate our method's effectiveness compared with pure IL methods, with comprehensive ablations confirming the contribution of each component.

