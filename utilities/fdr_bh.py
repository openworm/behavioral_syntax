# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 02:03:01 2015

@author: ltopuser
"""

# fdr_bh() - Executes the Benjamini & Hochberg (1995) and the Benjamini &
#            Yekutieli (2001) procedure for controlling the false discovery 
#            rate (FDR) of a family of hypothesis tests. FDR is the expected
#            proportion of rejected hypotheses that are mistakenly rejected 
#            (i.e., the null hypothesis is actually true for those tests). 
#            FDR is a somewhat less conservative/more powerful method for 
#            correcting for multiple comparisons than procedures like Bonferroni
#            correction that provide strong control of the family-wise
#            error rate (i.e., the probability that one or more null
#            hypotheses are mistakenly rejected).
#
# Usage:
#  >> [h, crit_p, adj_p]=fdr_bh(pvals,q,method,report);
#
# Required Input:
#   pvals - A vector or matrix (two dimensions or more) containing the
#           p-value of each individual test in a family of tests.
#
# Optional Inputs:
#   q       - The desired false discovery rate. {default: 0.05}
#   method  - ['pdep' or 'dep'] If 'pdep,' the original Bejnamini & Hochberg
#             FDR procedure is used, which is guaranteed to be accurate if
#             the individual tests are independent or positively dependent
#             (e.g., Gaussian variables that are positively correlated or
#             independent).  If 'dep,' the FDR procedure
#             described in Benjamini & Yekutieli (2001) that is guaranteed
#             to be accurate for any test dependency structure (e.g.,
#             Gaussian variables with any covariance matrix) is used. 'dep'
#             is always appropriate to use but is less powerful than 'pdep.'
#             {default: 'pdep'}
#   report  - ['yes' or 'no'] If 'yes', a brief summary of FDR results are
#             output to the MATLAB command line {default: 'no'}
#
#
# Outputs:
#   h       - A binary vector or matrix of the same size as the input "pvals."
#             If the ith element of h is 1, then the test that produced the 
#             ith p-value in pvals is significant (i.e., the null hypothesis
#             of the test is rejected).
#   crit_p  - All uncorrected p-values less than or equal to crit_p are 
#             significant (i.e., their null hypotheses are rejected).  If 
#             no p-values are significant, crit_p=0.
#   adj_p   - All adjusted p-values less than or equal to q are significant
#             (i.e., their null hypotheses are rejected). Note, adjusted 
#             p-values can be greater than 1.
#
#
# References:
#   Benjamini, Y. & Hochberg, Y. (1995) Controlling the false discovery
#     rate: A practical and powerful approach to multiple testing. Journal
#     of the Royal Statistical Society, Series B (Methodological). 57(1),
#     289-300.
#
#   Benjamini, Y. & Yekutieli, D. (2001) The control of the false discovery
#     rate in multiple testing under dependency. The Annals of Statistics.
#     29(4), 1165-1188.
#
# Example:
#   [dummy p_null]=ttest(randn(12,15)); #15 tests where the null hypothesis
#                                       #is true
#   [dummy p_effect]=ttest(randn(12,5)+1); #5 tests where the null
#                                          #hypothesis is false
#   [h crit_p adj_p]=fdr_bh([p_null p_effect],.05,'pdep','yes');
#
#
# For a review on false discovery rate control and other contemporary
# techniques for correcting for multiple comparisons see:
#
#   Groppe, D.M., Urbach, T.P., & Kutas, M. (2011) Mass univariate analysis 
# of event-related brain potentials/fields I: A critical tutorial review. 
# Psychophysiology, 48(12) pp. 1711-1725, DOI: 10.1111/j.1469-8986.2011.01273.x 
# http://www.cogsci.ucsd.edu/~dgroppe/PUBLICATIONS/mass_uni_preprint1.pdf
#
#
# Author:
# David M. Groppe
# Kutaslab
# Dept. of Cognitive Science
# University of California, San Diego
# March 24, 2010

# Copyright (c) 2010, David Groppe
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the distribution
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


################ REVISION LOG #################
#
# 5/7/2010-Added FDR adjusted p-values
# 5/14/2013- D.H.J. Poot, Erasmus MC, improved run-time complexity

function [h crit_p adj_p]=

def sort(array):
    sorted_array =np.sort(array)
    indices = np.argsort(array)
    return sorted_array, indices

def fdr_bh(*args):
    
    #pvals = arg[1]
    #q = arg[2]
    #method = arg[3]
    #adj_p = arg[4]
    
    #let's define the number of arguments:
    N = len(args)
    
    if N<1:
        raise Exception('You need to provide a vector or matrix of p-values.')
    else:
        if sum(pvals<0) > 0 :
            raise Exception('Some p-values are less than 0.')
        elif sum(pvals>1):
            raise Exception('Some p-values are greater than 1.')
    
    if N<2:
        pvals = arg[1]
        q=.05
    
    if N<3:
        pvals = arg[1]
        q = arg[2]
        method='pdep'
    
    if N<4:
        pvals = arg[1]
        q = arg[2]
        method = arg[3]
        report='no'
    
    s=np.shape(pvals)
    if (len(s)>2) or (s[0]>1):
        [p_sorted, sort_ids]= sort(pvals.reshape(1,np.product(s)))
    else
        #p-values are already a row vector
        [p_sorted, sort_ids]=sort(pvals)
        
    #indexes to return p_sorted to pvals order
    [dummy, unsort_ids]=sort(sort_ids) 
    m=len(p_sorted) #number of tests
    
    if method == 'pdep':
        #BH procedure for independence or positive dependence
        thresh=np.array(range(m))*q/m
        wtd_p=m*p_sorted*(1/np.array(range(m)))
        
    elif method == 'dep':
        #BH procedure for any dependency structure
        denom=m*sum(1/np.array(range(m)))
        thresh=np.array(range(m))*q/denom
        wtd_p=denom*p_sorted*(1/np.array(range(m)))
        #Note, it can produce adjusted p-values greater than 1!
        #compute adjusted p-values
    else:
        raise Exception('Argument ''method'' needs to be ''pdep'' or ''dep''.')
    
    #I'll assume that nargout>2 for all cases:
    #compute adjusted p-values
    adj_p=zeros(1,m)*NaN;
    [wtd_p_sorted, wtd_p_sindex] = sort( wtd_p )
    nextfill = 1;
    for k = 1 : m
        if wtd_p_sindex(k)>=nextfill
            adj_p(nextfill:wtd_p_sindex(k)) = wtd_p_sorted(k);
            nextfill = wtd_p_sindex(k)+1;
            if nextfill>m
                break;
            end;
        end;
    end;
    adj_p=reshape(adj_p(unsort_ids),s);
    end
    
    rej=p_sorted<=thresh;
    max_id=find(rej,1,'last'); #find greatest significant pvalue
    if isempty(max_id),
        crit_p=0;
        h=pvals*0;
    else
        crit_p=p_sorted(max_id);
        h=pvals<=crit_p;
    end
    
    if report == 'yes':
        n_sig=sum(p_sorted<=crit_p)
        if n_sig==1:
            print('Out of #d tests, #d is significant using a false discovery rate of #f.\n',m,n_sig,q);
        else
            print('Out of #d tests, #d are significant using a false discovery rate of #f.\n',m,n_sig,q)
        end
        if method == 'pdep':
            print('FDR procedure used is guaranteed valid for independent or positively dependent tests.\n')
        else:
            print('FDR procedure used is guaranteed valid for independent or dependent tests.\n')
    return h, crit_p, adj_p
