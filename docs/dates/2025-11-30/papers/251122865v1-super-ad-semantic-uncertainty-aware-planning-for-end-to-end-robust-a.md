---
layout: default
title: SUPER-AD: Semantic Uncertainty-aware Planning for End-to-End Robust Autonomous Driving
---

# SUPER-AD: Semantic Uncertainty-aware Planning for End-to-End Robust Autonomous Driving
**arXiv**：[2511.22865v1](https://arxiv.org/abs/2511.22865) · [PDF](https://arxiv.org/pdf/2511.22865.pdf)  
**作者**：Wonjeong Ryu, Seungjun Yu, Seokha Moon, Hojun Choi, Junsung Park, Jinkyu Kim, Hyunjung Shim  

**一句话要点**：提出语义不确定性感知规划框架，以提升仅摄像头端到端自动驾驶的鲁棒性。

**关键词**：端到端自动驾驶, 不确定性建模, BEV空间规划, 车道跟随正则化, 仅摄像头感知

## 3 点简述
- 核心问题：当前端到端自动驾驶系统忽略感知不确定性，在模糊场景中易失效。
- 方法要点：在BEV空间估计不确定性，结合车道跟随正则化，生成不确定性感知可行驶地图。
- 实验或效果：在NAVSIM基准测试中达到最优性能，显著提升NAVHARD和NAVSAFE子集表现。

## 摘要（原文）

> End-to-End (E2E) planning has become a powerful paradigm for autonomous driving, yet current systems remain fundamentally uncertainty-blind. They assume perception outputs are fully reliable, even in ambiguous or poorly observed scenes, leaving the planner without an explicit measure of uncertainty. To address this limitation, we propose a camera-only E2E framework that estimates aleatoric uncertainty directly in BEV space and incorporates it into planning. Our method produces a dense, uncertainty-aware drivability map that captures both semantic structure and geometric layout at pixel-level resolution. To further promote safe and rule-compliant behavior, we introduce a lane-following regularization that encodes lane structure and traffic norms. This prior stabilizes trajectory planning under normal conditions while preserving the flexibility needed for maneuvers such as overtaking or lane changes. Together, these components enable robust and interpretable trajectory planning, even under challenging uncertainty conditions. Evaluated on the NAVSIM benchmark, our method achieves state-of-the-art performance, delivering substantial gains on both the challenging NAVHARD and NAVSAFE subsets. These results demonstrate that our principled aleatoric uncertainty modeling combined with driving priors significantly advances the safety and reliability of camera-only E2E autonomous driving.

