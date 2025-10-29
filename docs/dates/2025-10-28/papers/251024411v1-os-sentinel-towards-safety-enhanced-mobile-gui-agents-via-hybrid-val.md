---
layout: default
title: OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows
---

# OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows
**arXiv**：[2510.24411v1](https://arxiv.org/abs/2510.24411) · [PDF](https://arxiv.org/pdf/2510.24411.pdf)  
**作者**：Qiushi Sun, Mukai Li, Zhoumianze Liu, Zhihui Xie, Fangzhi Xu, Zhangyue Yin, Kanzhi Cheng, Zehao Li, Zichen Ding, Qi Liu, Zhiyong Wu, Zhuosheng Zhang, Ben Kao, Lingpeng Kong  

**一句话要点**：提出OS-Sentinel框架，通过混合验证增强移动GUI代理在真实工作流中的安全性

**关键词**：移动GUI代理, 安全检测, 混合验证, 形式验证, VLM应用, 动态沙盒环境

## 3 点简述
- 移动GUI代理存在系统破坏和隐私泄露等不安全操作风险，检测挑战巨大
- 结合形式验证器和基于VLM的上下文判断器，实现混合安全检测
- 实验显示在多个指标上比现有方法提升10%-30%，促进更安全自主代理发展

## 摘要（原文）

> Computer-using agents powered by Vision-Language Models (VLMs) have
> demonstrated human-like capabilities in operating digital environments like
> mobile platforms. While these agents hold great promise for advancing digital
> automation, their potential for unsafe operations, such as system compromise
> and privacy leakage, is raising significant concerns. Detecting these safety
> concerns across the vast and complex operational space of mobile environments
> presents a formidable challenge that remains critically underexplored. To
> establish a foundation for mobile agent safety research, we introduce
> MobileRisk-Live, a dynamic sandbox environment accompanied by a safety
> detection benchmark comprising realistic trajectories with fine-grained
> annotations. Built upon this, we propose OS-Sentinel, a novel hybrid safety
> detection framework that synergistically combines a Formal Verifier for
> detecting explicit system-level violations with a VLM-based Contextual Judge
> for assessing contextual risks and agent actions. Experiments show that
> OS-Sentinel achieves 10%-30% improvements over existing approaches across
> multiple metrics. Further analysis provides critical insights that foster the
> development of safer and more reliable autonomous mobile agents.

