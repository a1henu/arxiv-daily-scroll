---
layout: default
title: Semantic Belief-State World Model for 3D Human Motion Prediction
---

# Semantic Belief-State World Model for 3D Human Motion Prediction
**arXiv**：[2601.03517v1](https://arxiv.org/abs/2601.03517) · [PDF](https://arxiv.org/pdf/2601.03517.pdf)  
**作者**：Sarim Chaudhry  

**一句话要点**：提出语义信念状态世界模型，通过潜在动力学模拟解决三维人体运动预测中的长期漂移问题。

**关键词**：三维人体运动预测, 信念状态世界模型, 潜在动力学模拟, SMPL-X参数化, 长期推演稳定性, 计算效率

## 3 点简述
- 传统方法将人体运动预测视为序列回归，导致长期预测时出现漂移和不确定性校准差。
- SBWM采用循环概率信念状态，独立学习动力学演化，并与SMPL-X解剖参数对齐，强制捕获运动动态。
- 实验显示SBWM能实现连贯的长期推演，在较低计算成本下保持竞争性精度。

## 摘要（原文）

> Human motion prediction has traditionally been framed as a sequence regression problem where models extrapolate future joint coordinates from observed pose histories. While effective over short horizons this approach does not separate observation reconstruction with dynamics modeling and offers no explicit representation of the latent causes governing motion. As a result, existing methods exhibit compounding drift, mean-pose collapse, and poorly calibrated uncertainty when rolled forward beyond the training regime. Here we propose a Semantic Belief-State World Model (SBWM) that reframes human motion prediction as latent dynamical simulation on the human body manifold. Rather than predicting poses directly, SBWM maintains a recurrent probabilistic belief state whose evolution is learned independently of pose reconstruction and explicitly aligned with the SMPL-X anatomical parameterization. This alignment imposes a structural information bottleneck that prevents the latent state from encoding static geometry or sensor noise, forcing it to capture motion dynamics, intent, and control-relevant structure. Inspired by belief-state world models developed for model-based reinforcement learning, SBWM adapts stochastic latent transitions and rollout-centric training to the domain of human motion. In contrast to RSSM-based, transformer, and diffusion approaches optimized for reconstruction fidelity, SBWM prioritizes stable forward simulation. We demonstrate coherent long-horizon rollouts, and competitive accuracy at substantially lower computational cost. These results suggest that treating the human body as part of the world models state space rather than its output fundamentally changes how motion is simulated, and predicted.

