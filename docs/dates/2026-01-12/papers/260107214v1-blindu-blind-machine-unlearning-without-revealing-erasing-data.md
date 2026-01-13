---
layout: default
title: BlindU: Blind Machine Unlearning without Revealing Erasing Data
---

# BlindU: Blind Machine Unlearning without Revealing Erasing Data
**arXiv**：[2601.07214v1](https://arxiv.org/abs/2601.07214) · [PDF](https://arxiv.org/pdf/2601.07214.pdf)  
**作者**：Weiqi Wang, Zhiyi Tian, Chenhan Zhang, Shui Yu  

**一句话要点**：提出BlindU方法，在联邦学习中实现无需上传原始数据的机器遗忘

**关键词**：机器遗忘, 联邦学习, 信息瓶颈, 隐私保护, 压缩表示

## 3 点简述
- 核心问题：现有机器遗忘方法需上传数据至服务器，与隐私保护场景如联邦学习冲突
- 方法要点：基于信息瓶颈机制生成压缩表示，结合专用遗忘模块和梯度下降算法实现遗忘
- 实验或效果：理论分析和实验表明BlindU在隐私保护和遗忘效果上优于现有基准

## 摘要（原文）

> Machine unlearning enables data holders to remove the contribution of their specified samples from trained models to protect their privacy. However, it is paradoxical that most unlearning methods require the unlearning requesters to firstly upload their data to the server as a prerequisite for unlearning. These methods are infeasible in many privacy-preserving scenarios where servers are prohibited from accessing users' data, such as federated learning (FL). In this paper, we explore how to implement unlearning under the condition of not uncovering the erasing data to the server. We propose \textbf{Blind Unlearning (BlindU)}, which carries out unlearning using compressed representations instead of original inputs. BlindU only involves the server and the unlearning user: the user locally generates privacy-preserving representations, and the server performs unlearning solely on these representations and their labels. For the FL model training, we employ the information bottleneck (IB) mechanism. The encoder of the IB-based FL model learns representations that distort maximum task-irrelevant information from inputs, allowing FL users to generate compressed representations locally. For effective unlearning using compressed representation, BlindU integrates two dedicated unlearning modules tailored explicitly for IB-based models and uses a multiple gradient descent algorithm to balance forgetting and utility retaining. While IB compression already provides protection for task-irrelevant information of inputs, to further enhance the privacy protection, we introduce a noise-free differential privacy (DP) masking method to deal with the raw erasing data before compressing. Theoretical analysis and extensive experimental results illustrate the superiority of BlindU in privacy protection and unlearning effectiveness compared with the best existing privacy-preserving unlearning benchmarks.

