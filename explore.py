
def plot_categorical_and_continuous_vars(df, categorical_var, continuous_var):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Box plot of categorical vs. continuous variable
    #use sample size
    sns.boxplot(x=categorical_var, y=continuous_var, data=df.sample(1000), ax=axes[0])
    axes[0].set_title(f'{continuous_var} vs. {categorical_var}')

    # Violin plot of categorical vs. continuous variable
    # use sample size
    sns.violinplot(x=categorical_var, y=continuous_var, data=df.sample(1000), ax=axes[1])
    axes[1].set_title(f'{continuous_var} vs. {categorical_var}')

     #Swarm plot of categorical vs. continuous variable, 
     #use sample size 
    sns.swarmplot(x=categorical_var, y=continuous_var, data=df.sample(1000), ax=axes[2])
    axes[2].set_title(f'{continuous_var} vs. {categorical_var}')


    plt.show()
    
categorical_var = 'fips'  
continuous_var = 'taxvaluedollarcnt'  

plot_categorical_and_continuous_vars(df, categorical_var, continuous_var)
    

    
def plot_variable_pairs(df):
    sns.pairplot(df)
    plt.show()
    

def explore_plot_variable_pairs(df):
    sns.pairplot(df, kind="reg", plot_kws={'line_kws':{'color':'red'}})
    plt.show()

def explore_plot_categorical_and_continuous_vars(df, cat_var, cont_var):
    plt.figure(figsize=(16, 6))

    # Boxplot
    plt.subplot(131)
    sns.boxplot(data=df, x=cat_var, y=cont_var)
    plt.title('Boxplot')

    # Violinplot
    plt.subplot(132)
    sns.violinplot(data=df, x=cat_var, y=cont_var)
    plt.title('Violinplot')

    # Barplot
    plt.subplot(133)
    sns.barplot(data=df, x=cat_var, y=cont_var)
    plt.title('Barplot')

    plt.show()